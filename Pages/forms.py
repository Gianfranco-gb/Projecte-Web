from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

from Pages.models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CircuitForm(ModelForm):
    class Meta:
        model = Circuit
        exclude = ("user",)


class ScuderiaForm(ModelForm):
    class Meta:
        model = Scuderia
        exclude = ("user",)


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        exclude = ("user",)


class SeasonForm(ModelForm):
    class Meta:
        model = Season
        exclude = ("user",)


class StatForm(ModelForm):
    class Meta:
        model = StatisticsDriver
        exclude = ("user",)