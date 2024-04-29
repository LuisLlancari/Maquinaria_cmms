import json
from django.shortcuts import render
from programacion_labor.models import Programacion
from django.contrib.auth.decorators import login_required

def obtener_usuarios():
    return Programacion.objects.values('idusuario', 'idusuario__username').distinct()

def obtener_tipos_labor():
    return Programacion.objects.values('idtipolabor', 'idtipolabor__tipolabor').distinct()

@login_required(login_url='login', redirect_field_name='home')
def home(request, datagrafic = None):
    usuario = request.user
    usuarios = obtener_usuarios()
    tipos_labor = obtener_tipos_labor()
    
    if datagrafic is not None:
        datagrafic = datagrafic.replace("'", '"')
    else:
        datagrafic = '[]'
    data = {
        'user': usuario,
        'usuarios': usuarios,
        'tipolabor': tipos_labor,
        'datagrafic' : datagrafic
    }
    print("Usuario logueado:", usuario)
    return render(request, 'core/home.html', data)

@login_required(login_url='login', redirect_field_name='home')
def test(request):
    return render(request, 'core/test.html')




















