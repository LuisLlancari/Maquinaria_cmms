from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import ConfiguracionTipoImplementoForms
from django.http import JsonResponse

#Manejo de errores
from django.contrib import messages


def configuracion(request):
  datos_configuracion = ConfiguracionTipoImplemento.objects.filter(estado=True)
  contexto = {
    'config': datos_configuracion,
    'form': ConfiguracionTipoImplementoForms
  }
  return render(request, 'componente_pieza/configuracion.html', contexto)

def registrarConfiguracion(request):
  if request.method == 'POST':
    form = ConfiguracionTipoImplementoForms(request.POST)
    if form.is_valid():
      form.save()
      return redirect('configuracion')
  else:
    messages.success(request, 'El formulario es inválido', extra_tags='danger')
  return redirect('configuracion')