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
from django.contrib import admin
from django.urls import path
from Pages import views
import formula1_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name = "Inicio"),
    path('Drivers', views.Drivers, name = "Drivers"),
    path('Circuits', views.Circuits, name = "Carreras"),
    path('Seasons', views.Seasons, name = "Temporadas"),
    path('Scuderia', views.Scuderia, name = "Escuderias"),
    path('Stats', views.Stats, name = "Estadisticas")
]