from django.shortcuts import render



def home(request):
	#tareas = Tarea.objects.all()
	#context = {'tareas': tareas}
	context = {}
	return render(request, 'home.html', context)