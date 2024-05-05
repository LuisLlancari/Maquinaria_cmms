from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from localizacion.models import Sede

#Manejo de errores
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='')
def fundo(request):
  fundos = Fundo.objects.filter(estado=True)
  sedes = Sede.objects.filter(estado=True)
  for fundo in fundos:
    #MANEJO DE ESTADO
    fundo.estado = 'Activo' if fundo.estado else 'Inactivo'
  return render(request, 'fundo_cultivo/fundo.html', {'datos': fundos,'sedes': sedes ,'form_fundo': FundoForm})

def registrar_fundo(request):
  if request.method == 'POST':
    form = FundoForm(request.POST)
    sede = request.POST.get('idsede')
    fundo = request.POST.get('fundo')
    fundo_existe = Fundo.objects.filter(fundo = fundo, idsede = sede, estado = True).exists()
    fundo_repite = Fundo.objects.filter(fundo = fundo, idsede = sede).exists()
                            #Si existe un registro      Si existe solo en fundo
    if form.is_valid() and fundo_existe == False  and fundo_repite == False:
      form.save()
      messages.success(request, 'Fundo registrado con exito', extra_tags='success')
      return redirect('fundo')
    else:
      messages.error(request, 'El fundo ya existe', extra_tags='danger')

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
                              #ID
    sede = request.POST.get('idsede')
    fundo = request.POST.get('fundo')
    fundo_existe = Fundo.objects.filter(fundo = fundo, idsede = sede, estado = True).exists()
    fundo_repite = Fundo.objects.filter(fundo = fundo, idsede = sede).exists()
                            #Si existe un registro      Si existe solo en fundo
    if form.is_valid() and fundo_existe == False and fundo_repite == False:
      form.save()
      messages.success(request, 'Fundo actualizado con exito', extra_tags='primary')
      return redirect('fundo')
    else:
      messages.error(request, 'Error al actualizar el fundo', extra_tags='danger')
  return redirect('fundo')
