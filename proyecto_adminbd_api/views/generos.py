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

class GeneroAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        genero = Generos.objects.filter(is_active = 1).order_by("id")
        lista = GeneroSerializer(genero, many=True).data
        
        return Response(lista, 200)

class GeneroView(generics.CreateAPIView):
    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        genero = get_object_or_404(Generos, id = request.GET.get("id"))
        genero = GeneroSerializer(genero, many=False).data

        return Response(genero, 200)
    
    #Registrar nuevo usuario
    @transaction.atomic
    def post(self,request, *args, **kwargs):

        genero = GeneroSerializer(data=request.data)
        if genero.is_valid():

            genero = Generos.objects.create(
                                        nombre_genero =request.data["nombre_genero"],
                                        is_active = 1)
            
            genero.save()

            return Response({"genero_created_id": genero.id }, 201)

        return Response(genero.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteGenero(generics.CreateAPIView):
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        genero = get_object_or_404(Generos, id=request.GET.get("id"))
        genero.is_active = 0
        genero.save()
        generos = GeneroSerializer(genero, many=False).data

        return Response(generos,200)
