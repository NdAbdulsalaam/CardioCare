from django.contrib import admin
from .models import User, HealthMetric, RiskAssessment, Recommendation, Reminder, ProgressTracking

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'gender', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'date_of_birth')

class HealthMetricsAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'blood_pressure', 'cholesterol_level', 'blood_sugar', 'created_at', 'updated_at')
    search_fields = ('user__username', 'height', 'weight', 'blood_pressure', 'cholesterol_level', 'blood_sugar')

class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'risk_level', 'assessment_date', 'details', 'created_at', 'updated_at')
    search_fields = ('user__username', 'risk_level', 'assessment_date')

class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommendation_type', 'details', 'created_at', 'updated_at')
    search_fields = ('user__username', 'recommendation_type')

class RemindersAdmin(admin.ModelAdmin):
    list_display = ('user', 'reminder_type', 'details', 'reminder_date', 'created_at', 'updated_at')
    search_fields = ('user__username', 'reminder_type', 'reminder_date')

class ProgressTrackingAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_type', 'goal_value', 'current_value', 'progress_date', 'created_at', 'updated_at')
    search_fields = ('user__username', 'goal_type', 'goal_value', 'current_value', 'progress_date')

# Register your models with custom admin configuration
admin.site.register(User, UserAdmin)
admin.site.register(HealthMetric, HealthMetricsAdmin)
admin.site.register(RiskAssessment, RiskAssessmentAdmin)
admin.site.register(Recommendation, RecommendationsAdmin)
admin.site.register(Reminder, RemindersAdmin)
admin.site.register(ProgressTracking, ProgressTrackingAdmin)