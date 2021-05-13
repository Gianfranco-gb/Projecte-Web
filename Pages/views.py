from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib import auth

from .forms import *
from .models import *
from django.views.generic.edit import CreateView


# Create your views here.
def home(request):
    return render(request, 'home.html')


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


# DRIVERS
def drivers(request):
    driver = Driver.objects.all()

    context = {'drivers': driver}
    return render(request, 'driver.html', context)


class driver_create(CreateView):
    model = Driver
    template_name = "form.html"
    form_class = DriverForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class driver_detail(DetailView):
    model = Driver
    template_name = 'driver_detail.html'

    def get_context_data(self, **kwargs):
        context = super(driver_detail, self).get_context_data(**kwargs)
        return context


# CIRCUIT
def circuits(request):
    circuit = Circuit.objects.all()
    context = {
        "circuits": circuit
    }
    return render(request, "circuit.html", context)


class circuit_create(CreateView):
    model = Circuit
    template_name = 'register.html'
    form_class = CircuitForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(circuit_create, self).form_valid(form)


class circuit_detail(DetailView):
    model = Circuit
    template_name = 'circuit_detail.html'

    def get_context_data(self, **kwargs):
        context = super(circuit_detail, self).get_context_data(**kwargs)
        return context


# SCUDERIA
def scuderias(request):
    scuderia = Scuderia.objects.all()
    context = {
        "scuderias": scuderia
    }
    return render(request, "scuderia.html", context)


class scuderia_create(CreateView):
    model = Scuderia
    template_name = 'register.html'
    form_class = ScuderiaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(scuderia_create, self).form_valid(form)


class scuderia_detail(DetailView):
    model = Scuderia
    template_name = 'scuderia_detail.html'

    def get_context_data(self, **kwargs):
        context = super(scuderia_detail, self).get_context_data(**kwargs)
        return context


# SEASONS
def seasons(request):
    season = Season.objects.all()
    context = {
        "seasons": season
    }
    return render(request, "season.html", context)


class season_create(CreateView):
    model = Season
    template_name = 'register.html'
    form_class = SeasonForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(season_create, self).form_valid(form)


class season_detail(DetailView):
    model = Season
    template_name = 'season_detail.html'

    def get_context_data(self, **kwargs):
        context = super(season_detail, self).get_context_data(**kwargs)
        return context


# STATS
def stats(request):
    stat = StatisticsDriver.objects.all()
    context = {
        "stats": stat
    }
    return render(request, "stat.html", context)


class stats_create(CreateView):
    model = StatisticsDriver
    template_name = 'register.html'
    form_class = StatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(stats_create, self).form_valid(form)


class stats_detail(DetailView):
    model = StatisticsDriver
    template_name = 'stat_detail.html'

    def get_context_data(self, **kwargs):
        context = super(stats_detail, self).get_context_data(**kwargs)
        return context
