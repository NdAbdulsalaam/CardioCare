from rest_framework import viewsets, generics
from .models import User, HealthMetric, RiskAssessment, Recommendation, Reminder, ProgressTracking
from .serializers import UserSerializer, HealthMetricsSerializer, RiskAssessmentSerializer, RecommendationsSerializer, RemindersSerializer, ProgressTrackingSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status

class UserRegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'date_of_birth': request.POST.get('date_of_birth'),
            'gender': request.POST.get('gender'),
            'password1': request.POST.get('password1'),
            'password2': request.POST.get('password2'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('user-login')  # Change this to the name of your login URL
        else: 
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'register.html', {'errors': errors})
    
class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            # return redirect('dashboard')  # Change this to the name of your dashboard URL
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'login.html', {'errors': errors})


class HealthMetricsView(generics.ListCreateAPIView):
    queryset = HealthMetric.objects.all()
    serializer_class = HealthMetricsSerializer

# class HealthMetricsViewSet(viewsets.ModelViewSet):
#     queryset = HealthMetric.objects.all()
#     serializer_class = HealthMetricsSerializer

class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer

class RecommendationsViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationsSerializer

class RemindersViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = RemindersSerializer

class ProgressTrackingViewSet(viewsets.ModelViewSet):
    queryset = ProgressTracking.objects.all()
    serializer_class = ProgressTrackingSerializer
