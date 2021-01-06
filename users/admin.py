from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['first_name', 'middle_name', 'last_name', 'email']
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
