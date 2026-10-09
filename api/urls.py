from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DeckViewSet, CardViewSet, CodingProblemViewSet, ExecuteCodeView,
    StudyReviewView, AnalyticsView, SeedDataView,
    RegisterView, LoginView, LogoutView, CurrentUserView
)

router = DefaultRouter()
router.register(r'decks', DeckViewSet, basename='deck')
router.register(r'cards', CardViewSet, basename='card')
router.register(r'coding-problems', CodingProblemViewSet, basename='coding-problem')

urlpatterns = [
    path('', include(router.urls)),
    path('code/execute/', ExecuteCodeView.as_view(), name='code-execute'),
    path('study/review/', StudyReviewView.as_view(), name='study-review'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('seed/', SeedDataView.as_view(), name='seed-data'),
    # Auth Endpoints
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/user/', CurrentUserView.as_view(), name='auth-user'),
]
