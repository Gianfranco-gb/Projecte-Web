from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def Inicio(request):
    return render(request, 'Pagina_Inici.html')


def Drivers(request):
    return HttpResponse("Drivers")


def Circuits(request):
    return HttpResponse("Carreras")


def Seasons(request):
    return HttpResponse("Calendario")


def Stats(request):
    return HttpResponse("Estadisticas")


def Scuderia(request):
    return HttpResponse("Escuderias")
