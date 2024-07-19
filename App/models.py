from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HealthMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    blood_pressure = models.CharField(max_length=50)
    cholesterol_level = models.FloatField()
    blood_sugar = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RiskAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    risk_level = models.CharField(max_length=50)
    assessment_date = models.DateField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recommendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_type = models.CharField(max_length=50)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reminders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_type = models.CharField(max_length=50)
    details = models.TextField()
    reminder_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProgressTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50)
    goal_value = models.FloatField()
    current_value = models.FloatField()
    progress_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
