from django.shortcuts import render

from .models import Cliente, IncidenciaNoIniciado


def home(request):
	context = {}
	return render(request, 'home.html', context)


def ticket_cliente(request):
	clientes = Cliente.objects.all()
	context = {'clientes': clientes}
	return render(request, 'ticket_cliente.html', context)



def ticket_general(request):
	IncidenciaNoIniciados = IncidenciaNoIniciado.objects.all()
	context = {'IncidenciaNoIniciados': IncidenciaNoIniciados}
	return render(request, 'ticket_general.html', context)
