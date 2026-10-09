from rest_framework import serializers
from .models import Deck, Card, ReviewLog, CodingProblem, UserCodeSubmission

class ReviewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLog
        fields = ['id', 'card', 'rating', 'interval_granted', 'ease_factor_after', 'reviewed_at']
        read_only_fields = ['id', 'reviewed_at']


class CardSerializer(serializers.ModelSerializer):
    is_due = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = [
            'id', 'deck', 'front', 'back', 'explanation', 'tags',
            'ease_factor', 'interval', 'repetitions', 'next_review_date',
            'last_reviewed_at', 'created_at', 'is_due'
        ]
        read_only_fields = ['id', 'ease_factor', 'interval', 'repetitions', 'next_review_date', 'last_reviewed_at', 'created_at']

    def get_is_due(self, obj):
        from django.utils import timezone
        return obj.next_review_date <= timezone.now()


class DeckSerializer(serializers.ModelSerializer):
    total_cards = serializers.IntegerField(read_only=True)
    due_cards_count = serializers.IntegerField(read_only=True)
    mastered_cards_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Deck
        fields = [
            'id', 'title', 'description', 'category', 'color_gradient', 'icon',
            'created_at', 'updated_at', 'total_cards', 'due_cards_count', 'mastered_cards_count'
        ]


class ReviewInputSerializer(serializers.Serializer):
    card_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=4)


# LEETCODE-STYLE CODING PRACTICE SERIALIZERS
class CodingProblemSerializer(serializers.ModelSerializer):
    submission_count = serializers.SerializerMethodField()

    class Meta:
        model = CodingProblem
        fields = [
            'id', 'title', 'category', 'difficulty', 'description',
            'language', 'initial_code', 'test_cases_json', 'submission_count'
        ]

    def get_submission_count(self, obj):
        return obj.submissions.count()


class CodeExecutionInputSerializer(serializers.Serializer):
    problem_id = serializers.IntegerField()
    code = serializers.CharField()
    language = serializers.CharField(default='python')


class UserCodeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCodeSubmission
        fields = ['id', 'user', 'problem', 'submitted_code', 'status', 'execution_time_ms', 'test_results_json', 'created_at']
