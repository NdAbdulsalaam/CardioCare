from rest_framework import viewsets, generics
from .models import User, HealthMetric, RiskAssessment, Recommendation, Reminder, ProgressTracking
from .serializers import UserSerializer, HealthMetricsSerializer, RiskAssessmentSerializer, RecommendationsSerializer, RemindersSerializer, ProgressTrackingSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .serializers import UserSerializer, LoginSerializer, UserProfileSerializer, ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.template.loader import render_to_string

class UserRegistrationView(APIView):
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
    
class UserLoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return redirect('user-profile')  # Change this to the name of your dashboard URL
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'login.html', {'errors': errors})

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return render(request, 'profile.html', {'serializer': serializer, 'user': user})

    def post(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('user-profile')
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return render(request, 'profile.html', {'serializer': serializer, 'user': user, 'errors': errors})
        
@login_required
def user_logout(request):
    logout(request)
    return redirect('user-login')

class ContactView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            # Send email
            send_mail(
                f'Contact Form Submission from {serializer.validated_data["name"]}',
                serializer.validated_data['message'],
                serializer.validated_data['email'],
                [settings.EMAIL_HOST_USER],  # To your email
                fail_silently=False,
            )
            return JsonResponse({"message": "Your message has been sent successfully."}, status=status.HTTP_200_OK)
        else:
            errors = [str(error) for error_list in serializer.errors.values() for error in error_list]
            return JsonResponse({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

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
