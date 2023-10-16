from django.urls import path
from formularioregistro import views as viewsregistro
from domys import views as viewsproject


urlpatterns = [
    path("registro/cliente/", viewsregistro.registrocliente, name="registro_cliente"),
    path("registro/negocio/", viewsregistro.registronegocio, name="registro_negocio"),
    path("registro/repartidor/", viewsregistro.registrorepartidor, name="registro_repartidor"),
    path("inicio/", viewsproject.inicio, name="inicio"),    
]