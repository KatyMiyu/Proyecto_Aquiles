from django.shortcuts import render
from .models import *

# Create your views here.


def informacion(request):
	nav_proveedores = Nav_proveedores.objects.all()
	informacion_proveedores = Informacion_proveedores.objects.all()
	context = {
		'nav_proveedores' : nav_proveedores,
		'informacion_proveedores' : informacion_proveedores
    }
	return render (request, 'proveedores/informacion.html', context)

def platos(request):
	nav_proveedores = Nav_proveedores.objects.all()
	platos_proveedores = Platos_proveedores.objects.all()
	context = {
		'nav_proveedores' : nav_proveedores,
		'platos_proveedores' : platos_proveedores
    }
	return render (request, 'proveedores/platos.html', context)
