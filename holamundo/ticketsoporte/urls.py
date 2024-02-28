from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("ticket_cliente/", views.ticket_cliente, name="ticket_cliente"),
    path("ticket_general/", views.ticket_general, name="ticket_general"),
    

]