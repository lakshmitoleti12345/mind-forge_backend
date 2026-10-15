from rest_framework import viewsets, status, permissions
from django.db import OperationalError as DjangoOperationalError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Deck, Card, ReviewLog, CodingProblem, UserCodeSubmission
from .serializers import (
    DeckSerializer, CardSerializer, ReviewLogSerializer, ReviewInputSerializer,
    CodingProblemSerializer, CodeExecutionInputSerializer, UserCodeSubmissionSerializer
)
from .algorithms import calculate_sm2
from .question_bank import QUESTION_BANK
from .coding_problems import CODING_PROBLEMS
from .code_evaluator import evaluate_code


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or request.user.is_superuser)


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all().order_by('-created_at')
    serializer_class = DeckSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=True, methods=['get'])
    def study(self, request, pk=None):
        deck = self.get_object()
        now = timezone.now()
        due_cards = Card.objects.filter(
            deck=deck
        ).filter(
            Q(next_review_date__lte=now) | Q(last_reviewed_at__isnull=True)
        ).order_by('next_review_date')

        if not due_cards.exists():
            due_cards = Card.objects.filter(deck=deck).order_by('next_review_date')[:15]

        serializer = CardSerializer(due_cards, many=True)
        return Response({
            'deck': DeckSerializer(deck).data,
            'count': due_cards.count(),
            'cards': serializer.data
        })


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('-created_at')
    serializer_class = CardSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        deck_id = self.request.query_params.get('deck', None)
        if deck_id:
            queryset = queryset.filter(deck_id=deck_id)
        return queryset


class CodingProblemViewSet(viewsets.ModelViewSet):
    queryset = CodingProblem.objects.all().order_by('id')
    serializer_class = CodingProblemSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]


class ExecuteCodeView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CodeExecutionInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        problem_id = serializer.validated_data['problem_id']
        submitted_code = serializer.validated_data['code']
        language = serializer.validated_data.get('language', 'python')

        try:
            problem = CodingProblem.objects.get(pk=problem_id)
        except CodingProblem.DoesNotExist:
            return Response({'error': 'Coding problem not found'}, status=status.HTTP_404_NOT_FOUND)

        eval_output = evaluate_code(
            submitted_code=submitted_code,
            test_cases=problem.test_cases_json,
            language=language
        )

        user_obj = request.user if request.user.is_authenticated else None
        submission_id = None
        try:
            submission = UserCodeSubmission.objects.create(
                user=user_obj,
                problem=problem,
                submitted_code=submitted_code,
                status=eval_output['status'],
                execution_time_ms=eval_output['execution_time_ms'],
                test_results_json=eval_output['results']
            )
            submission_id = submission.id
        except DjangoOperationalError:
            # Vercel read-only filesystem: DB write not possible on this
            # serverless instance. Return results without a persisted record.
            pass

        return Response({
            'submission_id': submission_id,
            'status': eval_output['status'],
            'passed_count': eval_output['passed_count'],
            'total_tests': eval_output['total_tests'],
            'execution_time_ms': eval_output['execution_time_ms'],
            'error_message': eval_output['error_message'],
            'results': eval_output['results']
        })


class StudyReviewView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ReviewInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        card_id = serializer.validated_data['card_id']
        rating = serializer.validated_data['rating']

        try:
            card = Card.objects.get(pk=card_id)
        except Card.DoesNotExist:
            return Response({'error': 'Card not found'}, status=status.HTTP_404_NOT_FOUND)

        new_reps, new_interval, new_ease, next_review = calculate_sm2(
            rating=rating,
            repetitions=card.repetitions,
            interval=card.interval,
            ease_factor=card.ease_factor
        )

        card.repetitions = new_reps
        card.interval = new_interval
        card.ease_factor = new_ease
        card.next_review_date = next_review
        card.last_reviewed_at = timezone.now()
        try:
            card.save()
            ReviewLog.objects.create(
                card=card,
                rating=rating,
                interval_granted=new_interval,
                ease_factor_after=new_ease
            )
        except DjangoOperationalError:
            # Vercel read-only filesystem: progress not persisted on this
            # serverless instance, but we still return correct SM-2 output.
            pass

        return Response({
            'message': 'Review recorded successfully',
            'card': CardSerializer(card).data,
            'interval_granted_days': new_interval,
            'next_review_date': next_review.isoformat()
        })


class AnalyticsView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        total_decks = Deck.objects.count()
        total_cards = Card.objects.count()
        total_problems = CodingProblem.objects.count()
        total_code_submissions = UserCodeSubmission.objects.count()
        accepted_code_submissions = UserCodeSubmission.objects.filter(status='Accepted').count()

        now = timezone.now()
        due_cards_count = Card.objects.filter(next_review_date__lte=now).count()
        mastered_cards_count = Card.objects.filter(interval__gt=21).count()
        total_reviews = ReviewLog.objects.count()

        ratings_summary = {
            'blackout': ReviewLog.objects.filter(rating=1).count(),
            'hard': ReviewLog.objects.filter(rating=2).count(),
            'good': ReviewLog.objects.filter(rating=3).count(),
            'easy': ReviewLog.objects.filter(rating=4).count(),
        }

        return Response({
            'total_decks': total_decks,
            'total_cards': total_cards,
            'due_cards': due_cards_count,
            'mastered_cards': mastered_cards_count,
            'total_reviews': total_reviews,
            'total_problems': total_problems,
            'total_code_submissions': total_code_submissions,
            'accepted_code_submissions': accepted_code_submissions,
            'ratings_summary': ratings_summary
        })


class SeedDataView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        category_gradients = {
            "Python Mastery": ("Backend Development", "from-emerald-600 to-teal-700", "Code"),
            "SQL & Database Mastery": ("Database & SQL", "from-indigo-600 to-blue-700", "Database"),
            "JavaScript Mastery": ("Frontend Core", "from-amber-500 to-orange-600", "Zap"),
            "React 19 Core": ("Frontend Frameworks", "from-cyan-500 to-blue-600", "Layers"),
            "Django REST Framework": ("Backend & APIs", "from-purple-600 to-indigo-700", "Server"),
        }

        created_cards_count = 0
        for subject_title, questions in QUESTION_BANK.items():
            cat_name, gradient, icon = category_gradients.get(subject_title, ("Engineering", "from-indigo-600 to-purple-600", "BookOpen"))
            deck, created = Deck.objects.get_or_create(
                title=subject_title,
                defaults={
                    'description': f'Complete 30 high-frequency interview questions for {subject_title}.',
                    'category': cat_name,
                    'color_gradient': gradient,
                    'icon': icon
                }
            )
            for q in questions:
                card_obj, card_created = Card.objects.get_or_create(
                    deck=deck,
                    front=q['front'],
                    defaults={
                        'back': q['back'],
                        'explanation': q.get('explanation', ''),
                        'tags': q.get('tags', '')
                    }
                )
                if card_created:
                    created_cards_count += 1

        created_problems_count = 0
        for prob in CODING_PROBLEMS:
            problem_obj, prob_created = CodingProblem.objects.get_or_create(
                title=prob['title'],
                defaults={
                    'category': prob['category'],
                    'difficulty': prob['difficulty'],
                    'description': prob['description'],
                    'language': prob['language'],
                    'initial_code': prob['initial_code'],
                    'solution_code': prob['solution_code'],
                    'test_cases_json': prob['test_cases']
                }
            )
            if prob_created:
                created_problems_count += 1

        return Response({
            'message': f'Seeded {created_cards_count} questions & {created_problems_count} LeetCode-style coding challenges!',
            'total_decks': Deck.objects.count(),
            'total_cards': Card.objects.count(),
            'total_coding_problems': CodingProblem.objects.count()
        }, status=status.HTTP_201_CREATED)


class RegisterView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')
        is_admin = request.data.get('is_admin', False)

        if not username or not password:
            return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            is_staff=is_admin,
            is_superuser=is_admin
        )

        return Response({
            'message': 'User registered successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_admin': user.is_staff
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials. Please check username and password.'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)

        return Response({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_admin': user.is_staff or user.is_superuser
            }
        })


class LogoutView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})


class CurrentUserView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                'is_authenticated': True,
                'user': {
                    'id': request.user.id,
                    'username': request.user.username,
                    'email': request.user.email,
                    'is_admin': request.user.is_staff or request.user.is_superuser
                }
            })
        return Response({'is_authenticated': False, 'user': None})
