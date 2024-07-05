from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import DetImplementos
from ..forms import DetImplementoForms
from django.http import JsonResponse

@login_required(login_url='login', redirect_field_name='')
def detalleImplemento (request):
  rol = request.user.idrol.rol
  if rol == "Admin":
    datos_detalle = DetImplementos.objects.filter(estado = True)
    return render(request, 'implemento/detalleimplemento.html', {'datos_detalle':datos_detalle, 'form': DetImplementoForms})
  else:
    return redirect('home')

@login_required(login_url='login', redirect_field_name='') 
def registrarDetalle(request):
  if request.method == 'POST':
    form = DetImplementoForms(request.POST)
    if form.is_valid(): 
      form.save()
      return redirect('detalleimplemento')
  else:
    return render(request, 'implemento/detalleimplemento.html', {})


@login_required(login_url='login', redirect_field_name='')
def eliminarDetalle(request, id_detalle):
  registro = get_object_or_404(DetImplementos, pk= id_detalle)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('detalleimplemento')
  

@login_required(login_url='login', redirect_field_name='')
def editarDetalle(request, id_detimplemento):
  implemento = get_object_or_404(DetImplementos, pk=id_detimplemento)
  form = DetImplementoForms(request.POST, instance=implemento)
  form.save()
  return redirect('detalleimplemento')


@login_required(login_url='login', redirect_field_name='')
def obtenerDatos(request, id_detimplemento):
  det_implemento = list(DetImplementos.objects.filter(pk=id_detimplemento).values())
  if(len(det_implemento) > 0):
    data = {'mensaje': "Success", 'det_implemento': det_implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
