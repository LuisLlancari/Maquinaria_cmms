from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Acciones
from ..forms import AccionesForms
from django.contrib import messages
from django.db.models import F
from django.http import JsonResponse


@login_required(login_url='login', redirect_field_name='')
def tareas(request):
  tareas = Acciones.objects.all()
  contexto = {
    'datos':tareas,
    'form': AccionesForms
  }
  return render(request, 'mantenimiento/tareas.html', contexto)

@login_required(login_url='login', redirect_field_name='')
def registrar_tareas(request):
  if request.method == 'POST':
    tareas_form = AccionesForms(request.POST)
    if tareas_form.is_valid():
      tareas_form.save()
      messages.success(request, 'Tarea registrada con exito', extra_tags='success')
      return redirect('tareas')
    else:
      messages.success(request, 'La tarea ya existe', extra_tags='danger')
      return redirect('tareas')
  
@login_required(login_url='login', redirect_field_name='')
def editar_tareas(request, id_tarea):
  if request.method == 'POST':
    tarea = get_object_or_404(Acciones, idaccion=id_tarea)

    tareas_form=AccionesForms(request.POST, instance=tarea)
    if tareas_form.is_valid():
      tareas_form.save()
      messages.success(request, 'Tarea editada con exito', extra_tags='primary')
      return redirect('tareas')
    else:
      messages.success(request, 'La tarea ya existe', extra_tags='danger')
      return redirect('tareas')

@login_required(login_url='login', redirect_field_name='')
def eliminar_tareas(request, id_tarea): 
  if request.method == 'POST':
    tarea = get_object_or_404(Acciones, idaccion=id_tarea)
    tarea.delete()
    return redirect('tareas')
  
@login_required(login_url='login', redirect_field_name='')
def obtenerDatos(request, id_tarea):
  tareas = get_object_or_404(Acciones,idaccion=id_tarea)

  datos = {
    'tarea': {
        'tarea': tareas.accion,
        'rol': tareas.estado
    }
  }
  return JsonResponse(datos)
  