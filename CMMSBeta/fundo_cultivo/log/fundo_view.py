from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from localizacion.models import Sede


@login_required(login_url='login', redirect_field_name='')
def fundo(request):
  fundos = Fundo.objects.filter(estado=True)
  sedes = Sede.objects.all()
  for fundo in fundos:
    #MANEJO DE ESTADO
    fundo.estado = 'Activo' if fundo.estado else 'Inactivo'
  return render(request, 'fundo_cultivo/fundo.html', {'datos': fundos,'sedes': sedes ,'form_fundo': FundoForm})

def registrar_fundo(request):
  form = FundoForm(request.POST)
  form.save()
  return redirect('fundo')

def eliminar_fundo(request, id_fundo):
  registro = get_object_or_404(Fundo, pk=id_fundo)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('fundo')
  
def editar_fundo(request):
  if request.method == 'POST':
    fundo_id = request.POST.get('fundo_id')
    fundo_instance = get_object_or_404(Fundo, pk=fundo_id)
    form = FundoForm(request.POST, instance=fundo_instance)
    if form.is_valid():
      form.save()
      return redirect('fundo')
    else:
      # Obtener los errores del formulario
      errores = form.errors.as_text()
      mensaje_error = f"Hubo un error en el formulario: {errores}"
      return HttpResponse(mensaje_error)
  else:
    return HttpResponse("La solicitud no fue valida")
