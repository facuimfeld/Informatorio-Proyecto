from django.db import models

# Create your models here.

class Servicio(models.Model): 
    nombre = models.CharField(max_length=100),
    imagen = models.ImageField(upload_to="varios", null=False)

class Registro_cliente(models.Model):
    nombre = models.CharField(max_length=40),
    apellido = models.CharField(max_length=40),
    telefono = models.IntegerField(max_length=10),
    direccion = models.CharField(max_length=50),
    email = models.EmailField()

class Registro_servicios(models.Model):
    nombre = models.CharField(max_length=40),
    apellido = models.CharField(max_length=40),
    telefono = models.IntegerField(max_length=10),
    direccion = models.CharField(max_length=50),
    email = models.EmailField(),
    matricula = models.BooleanField(),
    servicio = models.CharField(max_length=200)

    