from django.db import models

# Create your models here.

class Servicio(models.Model): 
    nombre = models.CharField(max_length=100,default='charfield')
    imagen = models.ImageField(upload_to="varios", null=False)

class Registro_cliente(models.Model):
    nombre = models.CharField(max_length=40,default='charfield')
    apellido = models.CharField(max_length=40, default='charfield')
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50,default='charfield')
    email = models.EmailField()

    #def __str__(self):
    #    return self.nombre

class Registro_servicios(models.Model):
    nombre = models.CharField(max_length=40,default='charfield')
    apellido = models.CharField(max_length=40,default='charfield')
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50,default='charfield')
    email = models.EmailField(default='charfield')
    matricula = models.BooleanField(default='charfield')
    servicio = models.CharField(max_length=200)

    #def __str__(self):
      #  return self.nombre
    