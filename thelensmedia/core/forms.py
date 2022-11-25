# forms for models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile

# class UserRegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField()
#     username = forms.CharField()
