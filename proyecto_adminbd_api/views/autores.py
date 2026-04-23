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

class AutorAll(generics.CreateAPIView):
    #Esta función es esencial para todo donde se requiera autorización de inicio de sesión (token)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        autor = Autores.objects.filter(is_active = 1).order_by("id")
        lista = AutorSerializer(autor, many=True).data
        
        return Response(lista, 200)

class AutorView(generics.CreateAPIView):
    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        autor = get_object_or_404(Autores, id = request.GET.get("id"))
        autor = AutorSerializer(autor, many=False).data

        return Response(autor, 200)
    
    #Registrar nuevo usuario
    @transaction.atomic
    def post(self,request, *args, **kwargs):

        autor = AutorSerializer(data=request.data)
        if autor.is_valid():

            autor = Autores.objects.create(
                                        first_name =request.data["first_name"],
                                        last_name = request.data["last_name"],
                                        nacionalidad = request.data["nacionalidad"],
                                        is_active = 1)
            
            autor.save()

            return Response({"autor_created_id": autor.id }, 201)

        return Response(autor.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAutor(generics.CreateAPIView):
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        autor = get_object_or_404(Autores, id=request.GET.get("id"))
        autor.is_active = 0
        autor.save()
        autores = AutorSerializer(autor, many=False).data

        return Response(autores,200)
