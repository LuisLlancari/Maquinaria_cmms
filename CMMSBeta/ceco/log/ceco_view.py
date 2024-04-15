from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Ceco
@login_required(login_url='login', redirect_field_name='')
def ceco(request):
    #usuario = request.user
    #print("Usuario logueado:", usuario)
    cecos = Ceco.objects.filter(estado=True)
    for ceco in cecos:
        ceco.estado = 'Activo' if ceco.estado else 'Inactivo'

    return render(request, 'ceco/ceco.html', {'datos': cecos, 'form_ceco': CecoForm, })


@login_required(login_url='login', redirect_field_name='')
def registrar_ceco(request):
    form = CecoForm(request.POST)
    form.save()
    return redirect('ceco')

@login_required(login_url='login', redirect_field_name='')
def editar_ceco(request):
    if request.method == 'POST':
        ceco_id = request.POST.get('ceco_id')
        ceco_instance = get_object_or_404(Ceco, pk=ceco_id)
        form = CecoForm(request.POST, instance=ceco_instance)
        if form.is_valid():
            form.save()
            return redirect('ceco')
        else:
            # Obtener los errores del formulario
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")

@login_required(login_url='login', redirect_field_name='')
def eliminar_ceco(request, id_ceco):
    registro = get_object_or_404(Ceco, pk=id_ceco)
    if request.method == 'POST':
        registro.estado = False
        registro.save()
        return redirect('ceco')