from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from Pages.models import Driver
from django.forms.models import ModelForm


class DriverForm(ModelForm):

    class Meta:
        model = Driver
        exclude = ('user',)
