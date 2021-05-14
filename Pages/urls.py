"""formula1_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Pages import views
from django.contrib.auth.decorators import login_required
from Pages.views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('circuits/', login_required(views.circuits), name="circuit"),
    path('drivers/', login_required(views.drivers), name="driver"),
    path('scuderias/', login_required(views.scuderias), name="scuderia"),
    path('seasons/', login_required(views.seasons), name="season"),
    path('stats/', login_required(views.stats), name="stats"),
    path('circuit/create', login_required(circuit_create.as_view()), name="circuit_create"),
    path('scuderia/create', login_required(scuderia_create.as_view()), name="scuderia_create"),
    path('driver/create', login_required(driver_create.as_view()), name="driver_create"),
    path('season/create', login_required(season_create.as_view()), name="season_create"),
    path('stats/create', login_required(stats_create.as_view()), name="stats_create"),
    path('circuit/<int:pk>', circuit_detail.as_view(), name="circuit_detail"),
    path('scuderia/<int:pk>', scuderia_detail.as_view(), name="scuderia_detail"),
    path('driver/<int:pk>', driver_detail.as_view(), name="driver_detail"),
    path('season/<int:pk>', season_detail.as_view(), name="season_detail"),
    path('stats/<int:pk>', stats_detail.as_view(), name="stat_detail"),

    path('circuit/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Circuit,
             form_class=CircuitForm, template_name='form_circuit.html'),
         name='circuit_edit'),

    path('driver/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Driver,
             form_class=DriverForm, template_name='form_driver.html'),
         name='driver_edit'),

    path('scuderia/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Driver,
             form_class=DriverForm, template_name='register.html'),
         name='scuderia_edit'),
]
