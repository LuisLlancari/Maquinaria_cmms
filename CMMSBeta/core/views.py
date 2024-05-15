import json
from django.shortcuts import render
from programacion_labor.models import Programacion
from django.contrib.auth.decorators import login_required
from usuario.models import * 
from programacion_labor.models import *
from implemento.models import *
from django.core.paginator import Paginator

def obtener_usuarios():
    return Usuario.objects.filter(idrol = 2)

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
    print(list(usuarios))
    return render(request, 'core/home.html', data)

@login_required(login_url='login', redirect_field_name='home')
def test(request):
    #
    lista_detalle = DetalleLabor.objects.all().order_by('-idprogramacion__fechahora')
    #paginator = Paginator(lista_detalle, 10)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    #paginador
    #page_obj = paginator.get_page(page_number)

    lista_implementos = Implemento.objects.all()
    #
    lista_supervisor = Usuario.objects.filter(idrol = 3)

    context = {
        'detlabor': lista_detalle,  # Pasar el objeto de la página a la plantilla
        'imple': lista_implementos,
        'list_sup': lista_supervisor
    }
    return render(request, 'core/test.html', context)





















