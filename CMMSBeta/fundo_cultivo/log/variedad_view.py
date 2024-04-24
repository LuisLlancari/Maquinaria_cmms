from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Variedad, Cultivo
from ..forms import VariedadForm

@login_required(login_url='login', redirect_field_name='')
def variedad(request):
  variedad = Variedad.objects.filter(estado=True)
  cultivo = Cultivo.objects.filter(estado=True)
  return render(request, 'fundo_cultivo/variedad.html',{'datos': variedad, 'cultivos' : cultivo ,'form_variedad': VariedadForm})


@login_required(login_url='login', redirect_field_name='')
def registrar_variedad(request):
    if request.method == 'POST':
        # Instanciamos el formulario
        form = VariedadForm(request.POST)

        # Validamos formulario
        if form.is_valid():
            
            # Obtenemos el valores de los inputs enviados por el request
            variedad_nombre = form.cleaned_data['variedad']
            id_cultivo = request.POST.get('idcultivo')

            # Validamos si el dato existe
            if Variedad.objects.filter(variedad=variedad_nombre, idcultivo=id_cultivo).exists():
                messages.success(request, "Datos ya existentes.", extra_tags='danger')
            else:
                messages.success(request, 'Variedad registrada con exito', extra_tags='success')
                form.save()
                
            # Retornamos la vista
            return redirect('variedad')
        else:
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")


def editar_variedad(request):
  if request.method == 'POST':
    variedad_id = request.POST.get('variedad_id')
    variedad_instance = get_object_or_404(Variedad, pk=variedad_id)
    form = VariedadForm(request.POST, instance=variedad_instance)
    if form.is_valid():
      form.save()
      messages.success(request, 'Variedad actualizada con exito', extra_tags='primary')
      return redirect('variedad')
    else:
      errores = form.errors.as_text()
      mensaje_error = f"Hubo un error en el formulario: {errores}"
      return HttpResponse(mensaje_error)
  return redirect('variedad')
  
  
def eliminar_variedad(request, id_variedad):
  registro = get_object_or_404(Variedad, pk=id_variedad)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('variedad')