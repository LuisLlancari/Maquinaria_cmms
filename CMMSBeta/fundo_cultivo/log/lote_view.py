from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

#Manejo de errores
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def lote(request):
  lotes = Lote.objects.filter(estado=True, idvariedad__estado=True)
  variedades = Variedad.objects.filter(estado=True)
  Cultivos = Cultivo.objects.filter(estado=True)
  return render(request, 'fundo_cultivo/lote.html',{'datos': lotes, 'variedades': variedades, 'cultivos': Cultivos, 'form_lote': LoteForm})

def registrar_lote(request):
  if request.method == 'POST':
    form = LoteForm(request.POST)
    if form.is_valid():
      lote = form.cleaned_data['lote']
      fundo = request.POST.get('idfundo')
      variedad = request.POST.get('idvariedad')

      if Lote.objects.filter(lote = lote, idvariedad = variedad, idfundo= fundo).exists():
        messages.success(request, ("Los datos ya existen."))
        print("datos repetidos")
        return redirect('lote')
      else:
        form.save()
        return redirect('lote')
    else:
      messages.success(request, ("Ingrese datos validos"))
      return redirect('lote')
  else:
    return redirect('lote')

def eliminar_lote(request, id_lote):
  registro = get_object_or_404(Lote, pk=id_lote)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('lote')
  
def obtener_lote(request):
  variedad = list(Variedad.objects.all().values())
  if(len(variedad) > 0):
    data = {'mensaje': "Success", 'variedad': variedad}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

def editar_lote(request):
  if request.method == 'POST':
    lote_id = request.POST.get('lote_id')
    lote_instance = get_object_or_404(Lote, pk=lote_id)
    form = LoteForm(request.POST, instance=lote_instance)
    if form.is_valid():
      form.save()
      messages.success(request, 'Lote actualizado con exito', extra_tags='primary')
      return redirect('lote')
    else:
      messages.error(request, 'La actualización fallo', extra_tags='danger')
  return redirect('lote')