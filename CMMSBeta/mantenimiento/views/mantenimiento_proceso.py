from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from implemento.models import DetImplementos, Implemento
from usuario.models import Persona
from mantenimiento.models import Mantenimiento, DetMotivos, Acciones, DetalleMantenimiento
from django.http import JsonResponse

def datos_mantenimiento(request):
  mantenimiento = list(Mantenimiento.objects.filter(fechaingreso__isnull=False, fechasalida__isnull=True, estado = 1).annotate(
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

  tareas = list(Acciones.objects.filter(estado = 0).values('idaccion','accion'))

  personas = list(Persona.objects.filter(estado = 1).values('idpersona', 'nombres', 'apellidos'))

  datos = {'mantenimientos': mantenimiento, 'tareas':tareas, 'personas':personas}
  return JsonResponse(datos)

def datos_implemento(request, id_programacion, id_implemento):
  pieza_implemento = list(DetImplementos.objects.filter(idimplemento = id_implemento).values())
  tareas_implemento = list(DetMotivos.objects.filter(idprogramacionmantenimiento = id_programacion).annotate(
    tarea= F('idaccion__accion'),
    idtarea= F('idaccion__idaccion')
  ).values('tarea', 'idtarea'))

  return JsonResponse({'partes': pieza_implemento, 'tareas':tareas_implemento})

def finalizar_mantenimiento(request, id_mantenimiento):
  if request.method == 'POST':
    encargado = request.POST.get('encargado')
    fecha_salida = request.POST.get('fecha-salida')
    tareas = request.POST.getlist('realizado')

    # Mantenimiento.objects.filter(idmantenimiento = id_mantenimiento).update(
    #   persona_id= encargado,
    #   fechasalida = fecha_salida,
    #   estado = 0
    # )
    mantenimiento = get_object_or_404(Mantenimiento,idmantenimiento = id_mantenimiento)
    # mantenimiento.persona_id = encargado
    # mantenimiento.fechasalida = fecha_salida
    # mantenimiento.estado = 0
    # mantenimiento.save()

    # implemento =mantenimiento.idprogramacionmantenimiento.idimplemento.idimplemento
    # Implemento.objects.filter(idimplemento = implemento).update(estado_actividad = 1) 

    # for tarea in tareas:
    #   DetalleMantenimiento.objects.create(
    #     idmantenimiento_id = id_mantenimiento,
    #     idaccion_id = tarea
    #   )

      
    
  return redirect('mantenimiento_proceso')

def detalle_mantenimiento (request, id_mantenimiento):
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento = id_mantenimiento).annotate(
    tareas = F('idaccion__accion'),
  ).values(
    'tareas',
    'completado'))
  return JsonResponse({'tareas': tareas})

def mantenimiento_proceso(request):
  return render(request, 'mantenimiento/completar_mantenimiento.html')
