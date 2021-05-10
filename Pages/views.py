from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import *
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Error wrong username/password')
    form = AuthenticationForm
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

def list_drivers(request, limit):
    queryset = Driver.objects.filter(date__lte=timezone.now()).order_by('-date')[:2]
    context = {
        "object" : queryset
    }
    return render(request, "list_driver,html", context)

def drivers(request):
    queryset = Driver.objects.all()
    context = {
        "object": queryset
    }
    return render(request, "driver.html", context)


def circuits(request):
    return render(request, 'circuit.html')


def seasons(request):
    return render(request, 'season.html')


def stats(request):
    return render(request, 'stats.html')


def scuderia(request):
    return render(request, 'scuderia.html')
