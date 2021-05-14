from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.contrib import auth

from .forms import *
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = ''


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
    return render(request, 'driver/driver.html', context)


class driver_create(CreateView):
    model = Driver
    template_name = "driver/form_driver.html"
    form_class = DriverForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class driver_detail(DetailView):
    model = Driver
    template_name = 'driver/driver_detail.html'

    def get_context_data(self, **kwargs):
        context = super(driver_detail, self).get_context_data(**kwargs)
        return context


def driver_delete_view(request, pk):
    context = {}

    obj = get_object_or_404(Driver, id=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/drivers/")

    return render(request, "confirm_delete.html", context)


# CIRCUIT
def circuits(request):
    circuit = Circuit.objects.all()
    context = {
        "circuits": circuit
    }
    return render(request, "circuit/circuit.html", context)


class circuit_create(CreateView):
    model = Circuit
    template_name = 'circuit/form_circuit.html'
    form_class = CircuitForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(circuit_create, self).form_valid(form)


class circuit_detail(DetailView):
    model = Circuit
    template_name = 'circuit/circuit_detail.html'

    def get_context_data(self, **kwargs):
        context = super(circuit_detail, self).get_context_data(**kwargs)
        return context


def circuit_delete_view(request, pk):
    context = {}

    obj = get_object_or_404(Circuit, id=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/circuits/")

    return render(request, "confirm_delete.html", context)


# SCUDERIA
def scuderias(request):
    scuderia = Scuderia.objects.all()
    context = {
        "scuderias": scuderia
    }
    return render(request, "scuderia/scuderia.html", context)


class scuderia_create(CreateView):
    model = Scuderia
    template_name = 'register.html'
    form_class = ScuderiaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(scuderia_create, self).form_valid(form)


class scuderia_detail(DetailView):
    model = Scuderia
    template_name = 'scuderia/scuderia_detail.html'

    def get_context_data(self, **kwargs):
        context = super(scuderia_detail, self).get_context_data(**kwargs)
        return context


def scuderia_delete_view(request, pk):
    context = {}

    obj = get_object_or_404(Scuderia, id=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/scuderias/")

    return render(request, "confirm_delete.html", context)


# SEASONS
def seasons(request):
    season = Season.objects.all()
    context = {
        "seasons": season
    }
    return render(request, "season/season.html", context)


class season_create(CreateView):
    model = Season
    template_name = 'season/form_season.html'
    form_class = SeasonForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(season_create, self).form_valid(form)


class season_detail(DetailView):
    model = Season
    template_name = 'season/season_detail.html'

    def get_context_data(self, **kwargs):
        context = super(season_detail, self).get_context_data(**kwargs)
        return context


def season_delete_view(request, pk):
    context = {}

    obj = get_object_or_404(Season, id=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/seasons/")

    return render(request, "confirm_delete.html", context)


# STATS
def stats(request):
    stat = StatisticsDriver.objects.all()
    context = {
        "stats": stat
    }
    return render(request, "stats/stat.html", context)


class stats_create(CreateView):
    model = StatisticsDriver
    template_name = 'stats/form_stats.html'
    form_class = StatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(stats_create, self).form_valid(form)


class stats_detail(DetailView):
    model = StatisticsDriver
    template_name = 'stats/stat_detail.html'

    def get_context_data(self, **kwargs):
        context = super(stats_detail, self).get_context_data(**kwargs)
        return context


def stat_delete_view(request, pk):
    context = {}

    obj = get_object_or_404(StatisticsDriver, id=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/stats/")

    return render(request, "confirm_delete.html", context)