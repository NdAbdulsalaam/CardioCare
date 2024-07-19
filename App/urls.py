from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HealthMetricsViewSet, RiskAssessmentViewSet, RecommendationsViewSet, RemindersViewSet, ProgressTrackingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'health-metrics', HealthMetricsViewSet)
router.register(r'risk-assessments', RiskAssessmentViewSet)
router.register(r'recommendations', RecommendationsViewSet)
router.register(r'reminders', RemindersViewSet)
router.register(r'progress-tracking', ProgressTrackingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
