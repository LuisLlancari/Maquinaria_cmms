from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def lote(request):
  lotes = Lote.objects.filter(estado=True, idvariedad__estado=True, idcultivo__estado=True)
  variedades = Variedad.objects.filter(estado=True)
  Cultivos = Cultivo.objects.filter(estado=True)
  return render(request, 'fundo_cultivo/lote.html',{'datos': lotes, 'variedades': variedades, 'cultivos': Cultivos, 'form_lote': LoteForm})

def registrar_lote(request):
  form = LoteForm(request.POST)
  form.save()
  return redirect('lote')

def eliminar_lote(request, id_lote):
  registro = get_object_or_404(Lote, pk=id_lote)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('lote')
  
def editar_lote(request):
  if request.method == 'POST':
    lote_id = request.POST.get('lote_id')
    lote_instance = get_object_or_404(Lote, pk=lote_id)
    form = LoteForm(request.POST, instance=lote_instance)
    if form.is_valid():
      form.save()
      return redirect('lote')
    else:
      # Obtener los errores del formulario
      errores = form.errors.as_text()
      mensaje_error = f"Hubo un error en el formulario: {errores}"
      return HttpResponse(mensaje_error)
  else:
    return HttpResponse("La solicitud no fue valida")