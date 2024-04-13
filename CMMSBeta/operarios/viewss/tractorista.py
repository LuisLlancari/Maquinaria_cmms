from django.shortcuts import render, redirect, get_object_or_404
from ..models import Tractorista
from ..forms import TractoristaForms
from django.http import JsonResponse

def tractoristas(request):
  datos_tractoristas = Tractorista.objects.filter(estado = True)
  return render(request, 'operarios/tractoristas.html', {'datos_tractoristas':datos_tractoristas, 'form':TractoristaForms})

def registrarTractorista(request):
  form = TractoristaForms(request.POST)
  form.save()
  return redirect('tractorista')

def eliminarTractorista(request, id_tractorista):
  registro = get_object_or_404(Tractorista, pk= id_tractorista)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tractorista')

def editarTractoristas(request, id_tractorista):
  tractorista = get_object_or_404(Tractorista, pk=id_tractorista)
  form = TractoristaForms(request.POST, instance=tractorista)
  form.save()
  return redirect('tractorista')

def obtenerDatos(request, id_tractorista):
  tractorista = list(Tractorista.objects.filter(pk=id_tractorista).values())
  if(len(tractorista) > 0):
    data = {'mensaje': "Success", 'tractorista': tractorista}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)