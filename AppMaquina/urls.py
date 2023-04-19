from django.contrib import admin
from django.urls import path
from AppMaquina.views import *
# se importa el logout directamente al url
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', inicio, name = "inicio"),
    path('herramienta/', herramienta, name = "herramienta"),
    path('insumos/', insumos, name = "insumos"),
    path('repuestos/', repuestos, name = "repuestos"),
    path('tecnico/', tecnico, name = "tecnico"),
    # path('formulario/', herraFomulario, name = "herraFormulario"),
    # paginas nuevas
    path('busqueda/', busqueda, name = "busqueda"),

    path('busquedainsumos/', busquedainsumos, name = "busquedainsumos"),
    path('busquedaRepuestos/', busquedaRepuestos, name = "busquedaRepuestos"),
    # <-------------------------------------------------------------------->
    path('busquedaherra/', busquedaherra, name = "busquedaherra"),
    
    path('buscar/', buscar, name = "buscar"),
    # busqueda de repuestos e insumos
    path('buscarInsu/', buscarInsu, name = "buscarInsu"),
    path('buscarRepu/', buscarRepu, name = "buscarRepu"),
    # leer herramienta
    path('leerherramienta/', leerHerramienta, name = "leerHerramienta"),
    # eliminar herramienta
    path('eliminarHerra/<id>', eliminarHerra, name = "eliminarHerra"),
    path('editarHerra/<id>', editarHerra, name = "editarHerra"),
    # login
    path('login/', login_request, name = "login"),
    # register/
    path('register/', register, name = 'register'),
    # logout
    path('logout/', LogoutView.as_view(), name = 'logout'),
    # editar perfil
    path('editarPerfil/', editarPerfil, name='editarPerfil'),

]