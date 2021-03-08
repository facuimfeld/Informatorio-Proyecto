from django.shortcuts import render
from django.http import HttpResponse
from proyecto_web_servicios.models import Registro_servicios

# Create your views here.
def home(request):
    return render(request,"index.html")

def servicios(request):
    return render(request,"servicios.html")

def buscar(request):
    if request.GET["bus"]:
        mensaje="Estas buscando: %r" %request.GET["bus"]
        busqueda=request.GET["bus"]

        buscar=Registro_servicios.objects.filter(servicio__icontains=busqueda)  
        return render(request,"resultado_busqueda.html", {"Servicio":buscar,"query":busqueda})       
    else:
        mensaje="No hay ese tipo de servicio"
    return HttpResponse(mensaje)

def registro(request):
    return render(request,"registro.html")

def iniciar_sesion(request):
    return render(request,"iniciar_sesion.html")

def quienes_somos(request):
    return render(request,"quienes_somos.html")