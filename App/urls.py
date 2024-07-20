from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView, HealthMetricsView, RiskAssessmentViewSet,
    RecommendationsViewSet, RemindersViewSet, ProgressTrackingViewSet
)

router = DefaultRouter()
router.register(r'risk-assessments', RiskAssessmentViewSet)
router.register(r'recommendations', RecommendationsViewSet)
router.register(r'reminders', RemindersViewSet)
router.register(r'progress-tracking', ProgressTrackingViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('health-metrics/', HealthMetricsView.as_view(), name='health-metrics'),
    path('', include(router.urls)),
]

