from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Deck(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    category = models.CharField(max_length=100, default='General')
    color_gradient = models.CharField(max_length=100, default='from-blue-600 to-indigo-600')
    icon = models.CharField(max_length=50, default='BookOpen')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_cards(self):
        return self.cards.count()

    @property
    def due_cards_count(self):
        return self.cards.filter(next_review_date__lte=timezone.now()).count()

    @property
    def mastered_cards_count(self):
        return self.cards.filter(interval__gt=21).count()


class Card(models.Model):
    deck = models.ForeignKey(Deck, related_name='cards', on_delete=models.CASCADE)
    front = models.TextField(help_text="Front content of flashcard")
    back = models.TextField(help_text="Back content / answer of flashcard")
    explanation = models.TextField(blank=True, default='', help_text="Detailed explanation or code snippet")
    tags = models.CharField(max_length=255, blank=True, default='', help_text="Comma-separated tags")
    
    ease_factor = models.FloatField(default=2.5)
    interval = models.IntegerField(default=0)
    repetitions = models.IntegerField(default=0)
    next_review_date = models.DateTimeField(default=timezone.now)
    last_reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Card #{self.id} ({self.deck.title}): {self.front[:30]}"


class ReviewLog(models.Model):
    RATING_CHOICES = [(1, 'Blackout'), (2, 'Hard'), (3, 'Good'), (4, 'Easy')]
    card = models.ForeignKey(Card, related_name='review_logs', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    interval_granted = models.IntegerField(default=0)
    ease_factor_after = models.FloatField(default=2.5)
    reviewed_at = models.DateTimeField(auto_now_add=True)


# LEETCODE-STYLE CODING PRACTICE MODELS
class CodingProblem(models.Model):
    DIFFICULTY_CHOICES = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default='Python Algorithms')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Easy')
    description = models.TextField()
    language = models.CharField(max_length=30, default='python')
    initial_code = models.TextField()
    solution_code = models.TextField(blank=True, default='')
    test_cases_json = models.JSONField(default=list, help_text="List of input and expected_output dicts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.difficulty}] {self.title}"


class UserCodeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ForeignKey(CodingProblem, related_name='submissions', on_delete=models.CASCADE)
    submitted_code = models.TextField()
    status = models.CharField(max_length=50, default='Accepted') # Accepted, Failed, Error
    execution_time_ms = models.FloatField(default=0.0)
    test_results_json = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission #{self.id} for {self.problem.title} ({self.status})"
