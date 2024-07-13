from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
	nav_administrador = Nav_administrador.objects.all()
	context = {
		
		'nav_administrador' : nav_administrador
		
    }
	return render (request, 'administrador/inicio.html', context)

def platos(request):
	nav_administrador = Nav_administrador.objects.all()
	platos_administrador = Platos_administrador.objects.all()
	context = {
		'platos_administrador' : platos_administrador,
		'nav_administrador' : nav_administrador
		
    }
	return render (request, 'administrador/platos.html', context)

def proveedores(request):
	nav_administrador = Nav_administrador.objects.all()
	informacion_proveedores = Proveedores_administrador.objects.all()

	context = {
		'informacion_proveedores' : informacion_proveedores,
		'nav_administrador' : nav_administrador
    }
	return render (request, 'administrador/proveedores.html', context)

def convenios(request):
	nav_administrador = Nav_administrador.objects.all()
	convenios_administrador = Convenios_administrador.objects.all()
	context = {
		'convenios_administrador' : convenios_administrador,
		'nav_administrador' : nav_administrador
		
    }
	return render (request, 'administrador/convenios.html', context)

def estadisticas(request):
	nav_administrador = Nav_administrador.objects.all()
	estadisticas_administrador = Estadisticas_administrador.objects.all()
	context = {
		'estadisticas_administrador' : estadisticas_administrador,
		'nav_administrador' : nav_administrador
		
    }
	return render (request, 'administrador/estadisticas.html', context)
