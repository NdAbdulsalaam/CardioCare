from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IndexView, UserRegistrationView, UserLoginView, UserProfileView,
    user_logout, ContactView,
    
    HealthMetricsView, RiskAssessmentViewSet,
    RecommendationsViewSet, RemindersViewSet, ProgressTrackingViewSet
)

router = DefaultRouter()
router.register(r'risk-assessments', RiskAssessmentViewSet)
router.register(r'recommendations', RecommendationsViewSet)
router.register(r'reminders', RemindersViewSet)
router.register(r'progress-tracking', ProgressTrackingViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('logout/', user_logout, name='user-logout'),
    path('contact/', ContactView.as_view(), name='user-contact'),
    path('health-metrics/', HealthMetricsView.as_view(), name='health-metrics'),
    
    path('', include(router.urls)),
]

