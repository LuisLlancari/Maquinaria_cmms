from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import PiezaForms
from django.http import JsonResponse


#Manejo de errores
from django.contrib import messages


def piezas(request):
  datos_piezas = Pieza.objects.filter(estado =True)
  #print(datos_piezas)
  contexto = {
    'datos_piezas': datos_piezas,
    'form': PiezaForms
  }
  return render(request, 'componente_pieza/piezas.html', contexto)

def registrarPieza(request):
  if request.method == 'POST':
    form = PiezaForms(request.POST)
    codigo = request.POST.get('codpieza')
    buscar = Pieza.objects.filter(codpieza = codigo,estado = True).exists()
    print(buscar)
    if form.is_valid():
      if buscar == False:
        form.save()
        messages.success(request, 'Pieza registrada con exito', extra_tags='success')
      else:
        messages.error(request, 'La pieza ya existe', extra_tags='danger')
      return redirect('pieza')
  else:
      messages.success(request, 'El formulario es inválido', extra_tags='danger')
  return redirect('pieza')

def eliminarPieza(request, id_pieza):
  registro = get_object_or_404(Pieza, pk= id_pieza)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    messages.success(request, 'Pieza eliminada con exito', extra_tags='success')
  else:
    messages.success(request, 'El formulario es inválido', extra_tags='danger')
  return redirect('pieza')
  
def editarPieza(request, id_pieza):
  pieza = get_object_or_404(Pieza, pk=id_pieza)
  form = PiezaForms(request.POST, instance=pieza)
  if form.is_valid():
    form.save()
    messages.success(request, 'Pieza editada con exito', extra_tags='success')
    return redirect('pieza')
  else:
    messages.success(request, 'El formulario es inválido', extra_tags='danger')
  return redirect('pieza')
    
def obtenerDatos(request, id_pieza):
  pieza = list(Pieza.objects.filter(pk=id_pieza).values())
  if(len(pieza) > 0):
    data = {'mensaje': "Success", 'pieza': pieza}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)