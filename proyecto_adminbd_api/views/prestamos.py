from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from proyecto_adminbd_api.serializers import *
from proyecto_adminbd_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json

class PrestamoAllnoFilter(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        prestamo = Prestamos.objects.order_by("id")
        lista = PrestamoSerializer(prestamo, many=True).data
        
        return Response(lista, 200)

class HitorialAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        prestamo = Prestamos.objects.filter(is_active = 0).order_by("id")
        lista = PrestamoSerializer(prestamo, many=True).data
        
        return Response(lista, 200)

class PrestamoAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        prestamo = Prestamos.objects.filter(is_active = 1).order_by("id")
        lista = PrestamoSerializer(prestamo, many=True).data
        
        return Response(lista, 200)

class PrestamoUserAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Clientes, id = request.GET.get("id"))
        prestamo = Prestamos.objects.filter(id_cliente = user.id).order_by("id")
        lista = PrestamoSerializer(prestamo, many=True).data
        
        return Response(lista, 200)

class PrestamoView(generics.CreateAPIView):
    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        prestamo = get_object_or_404(Prestamos, id = request.GET.get("id"))
        prestamo = PrestamoSerializer(prestamo, many=False).data

        return Response(prestamo, 200)
    
    #Registrar nuevo usuario
    @transaction.atomic
    def post(self,request, *args, **kwargs):

        prestamo = PrestamoSerializer(data=request.data)
        if prestamo.is_valid():

            prestamo = Prestamos.objects.create( 
                                        fecha_prestamo =request.data["fecha_prestamo"],
                                        fecha_devol_esperada =request.data["fecha_devol_esperada"],
                                        id_bibliotecario =request.data["id_bibliotecario"],
                                        id_libro =request.data["id_libro"],
                                        id_cliente =request.data["id_cliente"],
                                        estado = "en curso",
                                        is_active = 1)
            
            prestamo.save()

            return Response({"prestamo_created_id": prestamo.id }, 201)

        return Response(prestamo.errors, status=status.HTTP_400_BAD_REQUEST)

class LibroViewInactivo(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        libro = get_object_or_404(Libros, id_libro=request.data["id_libro"])
        libro.is_active = 0
        libro.veces_prestado += 1
        libro.save()
        libros = LibroSerializer(libro, many=False).data

        return Response(libros,200)

class LibroViewActivo(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        libro = get_object_or_404(Libros, id_libro=request.data["id_libro"])
        libro.is_active = 1
        libro.save()
        libros = LibroSerializer(libro, many=False).data

        return Response(libros,200)

class CantidadPrestamosClienteView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        cliente = get_object_or_404(Clientes, id=request.data["id"])
        cliente.prestamos_solicitados += 1
        cliente.save()
        clientes = ClienteSerializer(cliente, many=False).data

        return Response(clientes,200)


class PrestamosViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        prestamo = get_object_or_404(Prestamos, id=request.data["id"])
        prestamo.fecha_prestamo = request.data["fecha_prestamo"]
        prestamo.fecha_devol_esperada = request.data["fecha_devol_esperada"]
        prestamo.fecha_devol_real = request.data["fecha_devol_real"]
        prestamo.id_bibliotecario = request.data["id_bibliotecario"]
        prestamo.id_libro = request.data["id_libro"]
        prestamo.id_cliente = request.data["id_cliente"]
        prestamo.estado="terminado"
        prestamo.is_active=0
        prestamo.save()
        presta = PrestamoSerializer(prestamo, many=False).data

        return Response(presta,200)
    
    def delete(self, request, *args, **kwargs):
        prestamo = get_object_or_404(Prestamos, id=request.GET.get("id"))
        try:
            prestamo.delete()
            return Response({"details":"Prestamo eliminado"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)
