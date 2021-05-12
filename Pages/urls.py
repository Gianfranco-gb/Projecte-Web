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
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('circuit/', login_required(views.circuits), name="circuit"),
    path('driver/', login_required(views.drivers), name="driver"),
    path('scuderia/', login_required(views.scuderia), name="scuderia"),
    path('season/', login_required(views.seasons), name="season"),
    path('stats/', login_required(views.stats), name="stats"),
    path('circuit/create', login_required(circuit_create.as_view()), name="circuit_create"),
    path('scuderia/create', login_required(scuderia_create.as_view()), name="scuderia_create"),
    path('driver/create', login_required(driver_create.as_view()), name="driver_create"),

]
