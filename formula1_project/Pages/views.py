from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from .models import *
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

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
