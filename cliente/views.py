from django.shortcuts import render
from .models import *

# Create your views here.

def perfil(request):
	navs = Nav_cliente.objects.all()	
	context = {
		'navs' : navs
	}
	return render (request, 'cliente/perfil.html', context) 

def menu(request):
	navs = Nav_cliente.objects.all()	
	context = {
		'navs' : navs
	}
	return render (request, 'cliente/menu.html', context) 

def pedido(request):
	navs = Nav_cliente.objects.all()	
	context = {
		'navs' : navs
	}
	return render (request, 'cliente/pedido.html', context) 