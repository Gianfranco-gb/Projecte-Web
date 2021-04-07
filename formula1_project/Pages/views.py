from django.shortcuts import render, HttpResponse

# Create your views here.
def Inicio(request):

    #print("gdsfsd")
    return HttpResponse("Inicio")

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

