from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    model = CustomUser
    fields = ('first_name', 'middle_name', 'last_name', 'email',)

class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = ('fisrt_name', 'middle_name', 'last_name', 'email',)