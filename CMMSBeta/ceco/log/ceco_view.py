from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

#Manejo de errores
from django.contrib import messages

# Ceco
@login_required(login_url='login', redirect_field_name='')
def ceco(request):
    rol = request.user.idrol.rol
    if rol == "Admin":
        cecos = Ceco.objects.filter(estado=True)
        for ceco in cecos:
            ceco.estado = 'Activo' if ceco.estado else 'Inactivo'

        return render(request, 'ceco/ceco.html', {'datos': cecos, 'form_ceco': CecoForm, })
    else:
        return redirect('home')

@login_required(login_url='login', redirect_field_name='')
def registrar_ceco(request):
    if request.method == 'POST':
        form = CecoForm(request.POST)
        ceco = request.POST.get('ceco').strip()

        ceco_existe = Ceco.objects.filter(ceco = ceco, estado = True).exists()
        
        if form.is_valid() and ceco_existe == False:
            form.save()
            messages.success(request, 'Ceco registrado con éxito', extra_tags='success')
            return redirect('ceco')
        else:
            messages.error(request, 'El centro de costo ya existe', extra_tags='danger')

    return redirect('ceco')

@login_required(login_url='login', redirect_field_name='')
def editar_ceco(request):
    if request.method == 'POST':
        ceco_id = request.POST.get('ceco_id')
        ceco_instance = get_object_or_404(Ceco, pk=ceco_id)
        form = CecoForm(request.POST, instance=ceco_instance)

        ceco = request.POST.get('ceco').strip()
        ceco_existe = Ceco.objects.filter(ceco = ceco, estado = True).exists()
        if form.is_valid() and ceco_existe == False:
            form.save()
            messages.success(request, 'Ceco actualizado con éxito', extra_tags='primary')
            return redirect('ceco')
        else:
            messages.error(request, 'El centro de costo ya existe', extra_tags='danger')

    return redirect('ceco')

@login_required(login_url='login', redirect_field_name='')
def eliminar_ceco(request, id_ceco):
    registro = get_object_or_404(Ceco, pk=id_ceco)
    if request.method == 'POST':
        registro.estado = False
        registro.save()
        return redirect('ceco')