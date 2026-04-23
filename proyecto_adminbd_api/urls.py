"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_adminbd_api.views import bootstrap
from proyecto_adminbd_api.views import users
from proyecto_adminbd_api.views import clientes
from proyecto_adminbd_api.views import autores
from proyecto_adminbd_api.views import generos
from proyecto_adminbd_api.views import libros
from proyecto_adminbd_api.views import prestamos
from proyecto_adminbd_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Bibliotecarios
        path('bibliotecarios/', users.BiblioView.as_view()),
    #Create Clientes
        path('clientes/', clientes.ClienteView.as_view()),
     #Create Autores
        path('autores/', autores.AutorView.as_view()),
    #Create Generos
        path('generos/', generos.GeneroView.as_view()),
    #Create Libros
        path('libros/', libros.LibroView.as_view()),
    #Create Prestamos
        path('prestamos/', prestamos.PrestamoView.as_view()),
    #Lista bibliotecarios
        path('lista-bibliotecarios/', users.BiblioAll.as_view()),
    #Lista bibliotecarios
        path('lista-users/', users.UsersAll.as_view()),
    #Lista Clientes
        path('lista-clientes/', clientes.ClienteAll.as_view()),
    #Lista Clientes más activos
        path('lista-clientesmas/', clientes.ClientesMasActivossAll.as_view()),
    #Lista Autores
        path('lista-autores/', autores.AutorAll.as_view()),
    #Lista Generos
        path('lista-generos/', generos.GeneroAll.as_view()),
    #Lista Libros disponibles
        path('lista-libros/', libros.LibroAll.as_view()),
    #Lista Libros no disponibles
        path('lista-librosno/', libros.LibroAllNoDisponible.as_view()),
    #Lista Libros populares
        path('lista-librospo/', libros.LibrosPopularesAll.as_view()),
    #Lista Prestamos
        path('lista-prestamos/', prestamos.PrestamoAll.as_view()),
    #Lista Prestamos por cliente
        path('lista-prestamos-cliente/', prestamos.PrestamoUserAll.as_view()),
     #Lista Hitorial de prestamos
        path('historial/', prestamos.HitorialAll.as_view()),
    #Marcar un libro como inactivo
        path('libro-inactivo/', prestamos.LibroViewInactivo.as_view()),
    #Marcar un libro como Activo
        path('libro-activo/', prestamos.LibroViewActivo.as_view()),
    #Editar Prestamo
        path('prestamos-edit/', prestamos.PrestamosViewEdit.as_view()),
    #Delete User
        path('delete-user/', users.DeleteBiblio.as_view()),
    #Delete Genero
        path('delete-genero/', generos.DeleteGenero.as_view()),
    #Delete Cliente
        path('delete-cliente/', clientes.DeleteCliente.as_view()),
     #Delete Libro
        path('delete-libro/', libros.DeleteLibro.as_view()),
    #Delete Autor
        path('delete-autor/', autores.DeleteAutor.as_view()),
     #Incrementar prestamos realizados
        path('cliente-prestamos/', prestamos.CantidadPrestamosClienteView.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view())
]
