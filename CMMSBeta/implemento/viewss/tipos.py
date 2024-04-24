from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import TipoImplemento
from ..forms import TipoImplementoForms
from django.http import JsonResponse


#Manejo de errores
from django.contrib import messages

def tipoImplemento (request):
  datos_tipoimplemento = TipoImplemento.objects.filter(estado=True)
  return render(request, 'implemento/tipoimplemento.html', {'datos': datos_tipoimplemento, 'form': TipoImplementoForms})


def registrarTipoImplemento(request):
    if request.method == 'POST':
      form = TipoImplementoForms(request.POST)
      if form.is_valid(): 
        form.save()
        messages.success(request, 'Tipo de implemento registrado con exito', extra_tags='success')
        return redirect('tipoimplemento')
      else:
        messages.error(request, 'El tipo de implemento ya existe', extra_tags='danger')
    return redirect('tipoimplemento')

def eliminarImplemento(request, id):
  registro = get_object_or_404(TipoImplemento, pk= id)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tipoimplemento')
  
def editarTipoImplemento(request, id_tipo):
  if request.method == 'POST':
    tipo_implmento = get_object_or_404(TipoImplemento, pk=id_tipo)
    form = TipoImplementoForms(request.POST, instance=tipo_implmento)
    if form.is_valid():
      form.save()
      messages.success(request, 'Tipo de implemento editado con exito', extra_tags='primary')
      return redirect('tipoimplemento')
    else:
      messages.error(request, 'Error al editar', extra_tags='danger')
  return redirect('tipoimplemento')


def obtenerDatos(request, id_tipo):
  tipo_implemento = list(TipoImplemento.objects.filter(pk=id_tipo).values())
  if(len(tipo_implemento) > 0):
    data = {'mensaje': "Success", 'tipos': tipo_implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

