from rest_framework import serializers
from rest_framework.authtoken.models import Token
from proyecto_adminbd_api.models import *

#Selializador de Usuarios
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

#Selializador de Bibliotecarios
class BiblioSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Bibliotecarios
        fields = '__all__'

#Selializador de Clientes
class ClienteSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Clientes
        fields = '__all__'

#Selializador de Autores
class AutoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Autores
        fields = ('id','first_name','last_name')

class AutorSerializer(serializers.ModelSerializer):
    autor=AutoSerializer(read_only=True)
    class Meta:
        model = Autores
        fields = "__all__"
class AutoresAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'
        depth = 1

#Selializador de Generos
class GeneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    id_genero = serializers.CharField(required=True)
    nombre_genero = serializers.CharField(required=True)

    class Meta:
        model = Generos
        fields = ('id','id_genero','nombre_genero')

class GeneroSerializer(serializers.ModelSerializer):
    autor=GeneSerializer(read_only=True)
    class Meta:
        model = Generos
        fields = "__all__"
class GenerosAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'
        depth = 1

#Selializador de Libros
class LibSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    id_libro = serializers.CharField(required=True)
    titulo = serializers.CharField(required=True)

    class Meta:
        model = Libros
        fields = ('id','id_libro','titulo')

class LibroSerializer(serializers.ModelSerializer):
    autor=AutoSerializer(read_only=True)
    class Meta:
        model = Libros
        fields = "__all__"
class LibrosAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'
        depth = 1

#Selializador de Préstamos
class PreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    fecha_prestamo = serializers.CharField(required=True)

    class Meta:
        model = Prestamos
        fields = ('id','fecha_prestamo')

class PrestamoSerializer(serializers.ModelSerializer):
    prestamo=PreSerializer(read_only=True)
    class Meta:
        model = Prestamos
        fields = "__all__"
class PrestamosAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'
        depth = 1