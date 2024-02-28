from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    #path("cliente_agregar/", views.cliente_agregar, name="cliente_agregar"),

]