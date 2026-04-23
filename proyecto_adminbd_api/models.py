from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Bibliotecarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    direccion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return "Perfil del bibliotecario "+self.first_name+" "+self.last_name
    
class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255,null=True, blank=True)
    prestamos_solicitados = models.IntegerField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return "Perfil del cliente "+self.first_name+" "+self.last_name
    
class Autores(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255,null=True, blank=True)
    last_name = models.CharField(max_length=255,null=True, blank=True)
    nacionalidad = models.CharField(max_length=255,null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return "Autor: "+self.first_name+" "+self.last_name
    
class Generos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255,null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return "Autor: "+self.id+" "+self.nombre_genero
    
class Libros(models.Model):
    id_libro = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255,null=True, blank=True)
    id_autor = models.CharField(max_length=255,null=True, blank=True)
    id_genero = models.CharField(max_length=255,null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    fecha_registro = models.CharField(max_length=255,null=True, blank=True)
    veces_prestado = models.IntegerField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return "Autor: "+self.id+" "+self.titulo
    
class Prestamos(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_prestamo = models.CharField(max_length=255,null=True, blank=True)
    fecha_devol_esperada = models.CharField(max_length=255,null=True, blank=True)
    fecha_devol_real = models.CharField(max_length=255,null=True, blank=True)
    id_bibliotecario = models.CharField(max_length=255,null=True, blank=True)
    id_libro = models.CharField(max_length=255,null=True, blank=True)
    id_cliente = models.CharField(max_length=255,null=True, blank=True)
    estado = models.CharField(max_length=255,null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return "Prestamo: "+self.id+" "+self.fecha_prestamo