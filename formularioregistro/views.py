from django.shortcuts import render

# Create your views here.

def registrocliente(request):
    return render(request, "registrocliente.html")

def registronegocio(request):
    return render(request, "registronegocio.html")

def registrorepartidor(request):
    return render(request, "registrorepartidor.html")
