from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import DetalleComponenteForms
from django.http import JsonResponse


def det_componente(request):
  lista_componente = DetalleComponente.objects.filter(estado=True)
  contexto = {
    'lista_componente': lista_componente,
    'form': DetalleComponenteForms
    
  }
  return render(request, 'componente_pieza/det_componente.html', contexto)

def registrarDetalleComponente(request):
  if request.method == 'POST':
    form = DetalleComponenteForms(request.POST)
    if form.is_valid():
      form.save()
      return redirect('det_componente')
  else:
      form = DetalleComponenteForms()
      return render(request, 'componente_pieza/det_componente.html',{'form':form})