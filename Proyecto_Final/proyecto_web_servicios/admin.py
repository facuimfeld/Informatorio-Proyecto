from django.contrib import admin

from proyecto_web_servicios.models import Servicio
from proyecto_web_servicios.models import Registro_cliente
from proyecto_web_servicios.models import Registro_servicios

# Register your models here.

admin.register(Servicio)
admin.register(Registro_cliente)
admin.register(Registro_servicios)