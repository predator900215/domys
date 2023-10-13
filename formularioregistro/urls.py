from django.urls import path
from formularioregistro import views as viewsregistro


urlpatterns = [
    path("", viewsregistro.registrocliente, name="registro_cliente"),
]