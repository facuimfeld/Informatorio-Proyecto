from django.contrib import admin

from proyecto_web_servicios.models import Servicio
from proyecto_web_servicios.models import Registro_cliente
from proyecto_web_servicios.models import Registro_servicios

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display =("nombre","apellido")

admin.site.register(Servicio)
admin.site.register(Registro_cliente,ClientesAdmin)
admin.site.register(Registro_servicios,ClientesAdmin)