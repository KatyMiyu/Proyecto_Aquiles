from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
	navs = Nav_delivery.objects.all()	
	context = {
		'navs' : navs
	}
	return render (request, 'delivery/index.html', context) 

def info(request):
	navs = Nav_delivery.objects.all()	
	context = {
		'navs' : navs
	}
	return render (request, 'delivery/info.html', context) 