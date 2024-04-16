from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sistema
from ..forms import SistemaForms
from django.http import JsonResponse


def sistema(request):
  datos_sistema = Sistema.objects.filter(estado=True)
  return render(request, 'componente_pieza/sistema.html',{'datos_sistema':datos_sistema, 'form':SistemaForms})

def registrarSistema(request):
  if request.method == 'POST':
    form = SistemaForms(request.POST)
    if form.is_valid():
      form.save()
      return redirect('sistema')
  else:
      form = SistemaForms()
      return render(request, 'componente_pieza/sistema.html',{'form':form})


def eliminarSistema(request, id_sistema):
  registro = get_object_or_404(Sistema, pk= id_sistema)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('sistema')
  
def editarSistema(request, id_sistema):
  sistema = get_object_or_404(Sistema, pk=id_sistema)
  form = SistemaForms(request.POST, instance=sistema)
  form.save()
  return redirect('sistema')


def obtenerDatos(request, id_sistema):
  componentes = list(Sistema.objects.filter(pk = id_sistema).values())
  if(len(componentes) > 0):
    data = {'mensaje': "Success", 'componentes': componentes}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)