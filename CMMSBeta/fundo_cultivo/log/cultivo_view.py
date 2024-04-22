from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def cultivo(request):
  cultivos = Cultivo.objects.filter(estado=True)
  return render(request, 'fundo_cultivo/cultivo.html',{'datos': cultivos, 'form_cultivo': CultivoForm})

def registrar_cultivo(request):
  form = CultivoForm(request.POST)
  form.save()
  return redirect('cultivo')

def editar_cultivo(request):
  if request.method == 'POST':
    cultivo_id = request.POST.get('cultivo_id')
    cultivo_instance = get_object_or_404(Cultivo, pk=cultivo_id)
    form = CultivoForm(request.POST, instance=cultivo_instance)
    if form.is_valid():
      form.save()
      return redirect('cultivo')
    else:
      # Obtener los errores del formulario
      errores = form.errors.as_text()
      mensaje_error = f"Hubo un error en el formulario: {errores}"
      return HttpResponse(mensaje_error)
  else:
    return HttpResponse("La solicitud no fue valida")
  
def eliminar_cultivo(request, id_cultivo):
  registro = get_object_or_404(Cultivo, pk=id_cultivo)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('cultivo')