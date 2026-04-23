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

class LibroAllNoDisponible(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        libro = Libros.objects.filter(is_active = 0).order_by("id_libro")
        lista = LibroSerializer(libro, many=True).data
        
        return Response(lista, 200)

class LibroAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        libro = Libros.objects.filter(is_active = 1).order_by("id_libro")
        lista = LibroSerializer(libro, many=True).data
        
        return Response(lista, 200)

class LibrosPopularesAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        libro = Libros.objects.order_by("-veces_prestado")[:5]
        lista = LibroSerializer(libro, many=True).data
        
        return Response(lista, 200)

class LibroView(generics.CreateAPIView):
    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        libro = get_object_or_404(Libros, id = request.GET.get("id_libro"))
        libro = LibroSerializer(libro, many=False).data

        return Response(libro, 200)
    
    #Registrar nuevo usuario
    @transaction.atomic
    def post(self,request, *args, **kwargs):

        libro = LibroSerializer(data=request.data)
        if libro.is_valid():

            libro = Libros.objects.create( 
                                        titulo =request.data["titulo"],
                                        id_autor =request.data["id_autor"],
                                        id_genero =request.data["id_genero"],
                                        is_active = 1,
                                        veces_prestado = 0,
                                        fecha_registro =request.data["fecha_registro"])
            
            libro.save()

            return Response({"libro_created_id": libro.id_libro }, 201)

        return Response(libro.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteLibro(generics.CreateAPIView):
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        libro = get_object_or_404(Libros, id_libro=request.GET.get("id_libro"))
        libro.is_active = 0
        libro.save()
        libros = LibroSerializer(libro, many=False).data

        return Response(libros,200)
