from django.shortcuts import render, redirect, get_object_or_404
from ..models import TipoSolicitante
from ..forms import TiposolicitanteForms
from django.http import JsonResponse

def tipoSolicitante(request):
  datos_tipos = TipoSolicitante.objects.filter(estado = True)
  return render(request, 'operarios/tiposolicitante.html', {'datos_tipos':datos_tipos, 'form':TiposolicitanteForms})

def registrartipoSolicitante(request):
  datos_tipos = TipoSolicitante.objects.filter(estado = True)
  if request.method == 'POST':
    form = TiposolicitanteForms(request.POST)
    if form.is_valid():
      form.save()
      return redirect('tiposolicitante')
  else:
    return render(request, 'operarios/tiposolicitante.html', {'datos_tipos':datos_tipos})

def eliminarTiposolicitante(request, id_tipo):
  registro = get_object_or_404(TipoSolicitante, pk= id_tipo)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tiposolicitante')

def editarTiposolicitante(request, id_tipo):
  tipoSolicitante = get_object_or_404(TipoSolicitante, pk=id_tipo)
  form = TiposolicitanteForms(request.POST, instance=tipoSolicitante)
  form.save()
  return redirect('tiposolicitante')

def obtenerDatos(request, id_tipo):
  tipo_solicitante = list(TipoSolicitante.objects.filter(pk=id_tipo).values())
  if(len(tipo_solicitante) > 0):
    data = {'mensaje': "Success", 'tipo_solicitante': tipo_solicitante}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
