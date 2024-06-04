from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.timezone import now
from implemento.models import DetImplementos
from usuario.models import Persona
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento, DetMotivos, Acciones, DetalleMantenimiento, Recambios
from django.http import JsonResponse

def datos_mantenimientos(request):
  mantenimiento = list(Mantenimiento.objects.filter(estado = 0).annotate(
  fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
  tipomantenimiento = F('idprogramacionmantenimiento__tipomantenimiento'),
  implemento = F('idprogramacionmantenimiento__idimplemento__implemento'),
  cod_implemento = F('idprogramacionmantenimiento__idimplemento__codimplemento'),
  idprogramacion = F('idprogramacionmantenimiento__idprogramacionmantenimiento'),
  idimplemento = F('idprogramacionmantenimiento__idimplemento__idimplemento'),
  nombres = F(f'persona__nombres'),
  apellidos = F(f'persona__apellidos')
  ).values(
    'idmantenimiento',
    'idprogramacion',
    'fecha_programada',
    'implemento',
    'cod_implemento',
    'idimplemento',
    'tipomantenimiento',
    'fechaingreso',
    'fechasalida',
    'descripcion',
    'persona',
    'nombres',
    'apellidos',
    'fechaingreso',
    'estado'
    ))


  datos = {'mantenimientos': mantenimiento}
  return JsonResponse(datos)

def detalle_mantenimiento (request, id_mantenimiento):
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento = id_mantenimiento).annotate(
    tareas = F('idaccion__accion'),
  ).values(
    'tareas',
    'completado'))
  
  recambios = list(Recambios.objects.filter(idmantenimiento= id_mantenimiento).values())

  return JsonResponse({'tareas': tareas, 'recambios':recambios})

def mantenimientos_realizados(request):
  return render(request, 'mantenimiento/mantenimientos_realizados.html')

