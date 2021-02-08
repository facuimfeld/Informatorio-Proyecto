from django.db import models

# Create your models here.

class Servicio(models.Model): 
    nombre = models.CharField(max_length=100),
    imagen = models.ImageField(upload_to="varios", null=False)