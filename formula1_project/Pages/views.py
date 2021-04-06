from django.shortcuts import render, HttpResponse

# Create your views here.
def Inicio(request):

    print("gdsfsd")
    return HttpResponse("Inicio")

def Pilotos(request):

    return HttpResponse("Pilotos")

def Carreras(request):

    return HttpResponse("Carreras")

def Calendario(request):

    return HttpResponse("Calendario")

