from django.shortcuts import render, redirect, get_object_or_404
from ..models import TipoSolicitante
from ..forms import TiposolicitanteForms
from django.http import JsonResponse
from django.contrib import messages

def tipoSolicitante(request):
  datos_tipos = TipoSolicitante.objects.filter(estado = True)
  return render(request, 'operarios/tiposolicitante.html', {'datos_tipos':datos_tipos, 'form':TiposolicitanteForms})

def registrartipoSolicitante(request):
  datos_tipos = TipoSolicitante.objects.filter(estado = True)
  if request.method == 'POST':
    form = TiposolicitanteForms(request.POST)
    tipoSolicitante = request.POST.get('tiposolicitante').strip()
    tipoSolicitante_existe = TipoSolicitante.objects.filter(tiposolicitante = tipoSolicitante, estado = True).exists()
    if form.is_valid() and tipoSolicitante_existe == False:
      form.save()
      messages.success(request, "El tipo solicitante se ha agreado correctamente", extra_tags='success')
      return redirect('tiposolicitante')
    else:
      messages.success(request, "El tipo solicitante ya existe", extra_tags='warning')
      return redirect('tiposolicitante')
  else:
    return redirect('tiposolicitante')


def eliminarTiposolicitante(request, id_tipo):
  registro = get_object_or_404(TipoSolicitante, pk= id_tipo)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tiposolicitante')

def editarTiposolicitante(request, id_tipo):
  if request.method == 'POST':
    tipoSolicitante = get_object_or_404(TipoSolicitante, pk=id_tipo)
    form = TiposolicitanteForms(request.POST, instance=tipoSolicitante)

    tipoSolicitante = request.POST.get('tiposolicitante').lstrip()
    print(tipoSolicitante)
    tipoSolicitante_existe = TipoSolicitante.objects.filter(tiposolicitante = tipoSolicitante, estado = True).exists()
    print(tipoSolicitante_existe)
    if form.is_valid() and tipoSolicitante_existe == False:
      form.save()
      messages.success(request, "El tipo solicitante se ha modificado correctamente", extra_tags='primary')
      return redirect('tiposolicitante')
    else:
      messages.success(request, "No se pudo modificar el tipo solicitante", extra_tags='warning')
      return redirect('tiposolicitante')
    
  else:
      return redirect('tiposolicitante')


def obtenerDatos(request, id_tipo):
  tipo_solicitante = list(TipoSolicitante.objects.filter(pk=id_tipo).values())
  if(len(tipo_solicitante) > 0):
    data = {'mensaje': "Success", 'tipo_solicitante': tipo_solicitante}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
