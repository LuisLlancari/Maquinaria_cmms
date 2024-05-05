from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

#Manejo de errores
from django.contrib import messages

@login_required(login_url='login', redirect_field_name='')
def cultivo(request):
  cultivos = Cultivo.objects.filter(estado=True)
  return render(request, 'fundo_cultivo/cultivo.html',{'datos': cultivos, 'form_cultivo': CultivoForm})

def registrar_cultivo(request):
  if request.method == 'POST':
    #Manejo de caracteres el blanco 
    #.lstrip(): Elimina los espacios al principio
    #.rstrip(): Elimina los espacios al final
    #.strip(): Elimina los espacios al principio y al final
    cultivo = request.POST.get('cultivo').lstrip()
    existe_cultivo = Cultivo.objects.filter(cultivo = cultivo, estado = True).exists()
    form = CultivoForm(request.POST)
    if form.is_valid() and existe_cultivo == False:
      form.save()
      messages.success(request, 'Cultivo registrado con exito', extra_tags='success')
      return redirect('cultivo')
    else:
      messages.error(request, 'El cultivo ya existe', extra_tags='danger')
  return redirect('cultivo')

def editar_cultivo(request):
  if request.method == 'POST':
    cultivo_id = request.POST.get('cultivo_id')
    cultivo_instance = get_object_or_404(Cultivo, pk=cultivo_id)
    form = CultivoForm(request.POST, instance=cultivo_instance)

    cultivo = request.POST.get('cultivo').lstrip()
    existe_cultivo = Cultivo.objects.filter(cultivo = cultivo, estado = True).exists()
    if form.is_valid() and existe_cultivo == False:
      form.save()
      messages.success(request, 'Cultivo actualizado con exito', extra_tags='primary')
      return redirect('cultivo')
    else:
      messages.error(request, 'Error al actualizar el cultivo', extra_tags='danger')
  return redirect('cultivo')
  
def eliminar_cultivo(request, id_cultivo):
  registro = get_object_or_404(Cultivo, pk=id_cultivo)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('cultivo')