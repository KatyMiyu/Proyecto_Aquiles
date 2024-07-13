from django.urls import path, include
from . import views




urlpatterns = [
	path('perfil', views.perfil, name="perfil"),
    path('menu', views.menu, name="menu"),
    path('pedido', views.pedido, name="pedido"),
]
