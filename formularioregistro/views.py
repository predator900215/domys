from django.shortcuts import render

# Create your views here.

def registrocliente(request):
    return render(request, "registrocliente.html")
