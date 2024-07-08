from django.shortcuts import render

# Create your views here.


def home(request):
			context = {}
			return render (request, 'usuarios/home.html', context) 

def login(request):
			context = {}
			return render (request, 'usuarios/login.html', context)
def local(request):
			context = {}
			return render (request, 'usuarios/local.html', context)
