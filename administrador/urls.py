from django.urls import path, include
from . import views

urlpatterns = [
	path('inicio', views.inicio, name="inicio"),
    path('platos', views.platos, name="platos"),
    path('proveedores', views.proveedores, name="proveedores"),
    path('convenios', views.convenios, name="convenios"),
    path('estadisticas', views.estadisticas, name="estadisticas"),
]