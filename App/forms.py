from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'gender', 'password1', 'password2')
