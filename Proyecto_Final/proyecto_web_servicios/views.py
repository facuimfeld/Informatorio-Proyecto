from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def servicios(request):
    return render(request,"servicios.html")

def registro(request):
    return render(request,"registro.html")

def iniciar_sesion(request):
    return render(request,"iniciar_sesion.html")