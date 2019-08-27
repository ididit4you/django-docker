from django import forms
from django.contrib.auth.forms import (
    UsernameField, ReadOnlyPasswordHashField,
    UserCreationForm, UserChangeForm
)
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from .models import ProjectUser

class ProjectUserCreationForm(UserCreationForm):

    class Meta:
        model = ProjectUser
        fields = ("username",)
        field_classes = {'username': UsernameField}

class ProjectUserChangeForm(UserChangeForm):
    class Meta:
        model = ProjectUser
        fields = '__all__'
        field_classes = {'username': UsernameField}
