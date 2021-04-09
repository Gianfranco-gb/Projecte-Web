from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def log_in(request):
    return render(request, 'login.html')


def register(request):
    form = UserCreationForm
    return render(request, 'register.html', {"form": form})


def drivers(request):
    return HttpResponse("Drivers")


def circuits(request):
    return HttpResponse("Circuits")


def seasons(request):
    return HttpResponse("Seasons")


def stats(request):
    return HttpResponse("Statistics")


def scuderia(request):
    return HttpResponse("Scuderias")
