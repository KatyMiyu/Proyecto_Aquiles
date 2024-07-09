from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
	navs_home = Nav_home.objects.all()
	context = {
		'navs_home':navs_home
	}
	return render (request, 'usuarios/home.html', context) 

def login(request):
	navs_home = Nav_home.objects.all()
	
	context = {
		'navs_home':navs_home
	}
	return render (request, 'usuarios/login.html', context)


def local(request):
	navs_home = Nav_home.objects.all()
	context = {
		'navs_home':navs_home
	}
	return render (request, 'usuarios/local.html', context)
