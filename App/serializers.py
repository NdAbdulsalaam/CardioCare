from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, HealthMetric, RiskAssessment, Recommendation, Reminder, ProgressTracking

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'gender', 'password1', 'password2')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetric
        fields = '__all__'

class RiskAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = '__all__'

class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class RemindersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class ProgressTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracking
        fields = '__all__'
