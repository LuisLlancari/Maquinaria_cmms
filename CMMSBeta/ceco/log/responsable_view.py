from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import *  
from ..forms import *
from operarios.models import Encargado

@login_required(login_url='login', redirect_field_name='')
def responsable(request):
    responsable = Encargado.objects.filter()
    contexto = {
        'datos': responsable,
    }
    return render(request, 'ceco/responsable.html', contexto)

@login_required(login_url='login', redirect_field_name='')
def registrar_responsable(request):
    return redirect('responsable')

@login_required(login_url='login', redirect_field_name='')
def eliminar_responsable(request, id_responsable):
    return redirect('responsable')

@login_required(login_url='login', redirect_field_name='')
def editar_responsable(request):
    if request.method == 'POST':
        pass