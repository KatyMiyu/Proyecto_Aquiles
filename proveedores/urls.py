from django.urls import path, include
from . import views

urlpatterns = [
	
    path('informacion', views.informacion, name="informacion"),
    path('platos', views.platos, name="platos"),
]