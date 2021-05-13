from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *
from .models import *
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


# Create your views here.
def home(request):
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


def list_drivers(request):
    queryset = Driver.objects.filter(date__lte=timezone.now()).order_by('-date')[:2]
    context = {
        "object": queryset
    }
    return render(request, "list_driver,html", context)


def drivers(request):
    queryset = Driver.objects.all()
    context = {
        "object": queryset
    }
    return render(request, "driver.html", context)


class driver_create(CreateView):
    model = Driver
    template_name = "form.html"
    form_class = DriverForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def circuits(request):
    queryset = Circuit.objects.all()
    context = {
        "object": queryset
    }
    return render(request, "circuit.html", context)


class circuit_create(CreateView):
    model = Circuit
    template_name = 'register.html'
    form_class = CircuitForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(circuit_create, self).form_valid(form)


def scuderia(request):
    queryset = Scuderia.objects.all()
    context = {
        "object": queryset
    }
    return render(request, "scuderia.html", context)


class scuderia_create(CreateView):
    model = Scuderia
    template_name = 'register.html'
    form_class = ScuderiaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(scuderia_create, self).form_valid(form)


def seasons(request):
    return render(request, 'season.html')


def stats(request):
    return render(request, 'stats.html')


