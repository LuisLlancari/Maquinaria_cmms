from django.shortcuts import render, redirect, get_object_or_404
from ..models import DetImplementos
from ..forms import DetImplementoForms
from django.http import JsonResponse

def detalleImplemento (request):
  datos_detalle = DetImplementos.objects.filter(estado = True)
  return render(request, 'implemento/detalleimplemento.html', {'datos_detalle':datos_detalle, 'form': DetImplementoForms})

def registrarDetalle(request):
  if request.method == 'POST':
    form = DetImplementoForms(request.POST)
    if form.is_valid(): 
      form.save()
      return redirect('detalleimplemento')
  else:
    return render(request, 'implemento/detalleimplemento.html', {})

def eliminarDetalle(request, id_detalle):
  registro = get_object_or_404(DetImplementos, pk= id_detalle)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('detalleimplemento')
  
def editarDetalle(request, id_detimplemento):
  implemento = get_object_or_404(DetImplementos, pk=id_detimplemento)
  form = DetImplementoForms(request.POST, instance=implemento)
  form.save()
  return redirect('detalleimplemento')


def obtenerDatos(request, id_detimplemento):
  det_implemento = list(DetImplementos.objects.filter(pk=id_detimplemento).values())
  if(len(det_implemento) > 0):
    data = {'mensaje': "Success", 'det_implemento': det_implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
