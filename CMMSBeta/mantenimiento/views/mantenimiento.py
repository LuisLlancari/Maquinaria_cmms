from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.timezone import now
from implemento.models import DetImplementos
from usuario.models import Persona
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento, DetMotivos, Acciones, DetalleMantenimiento
from django.http import JsonResponse

def datos_mantenimiento(request):
  mantenimiento = list(Mantenimiento.objects.filter(estado = 1).annotate(
    fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
    tipomantenimiento = F('idprogramacionmantenimiento__tipomantenimiento'),
    implemento = F('idprogramacionmantenimiento__idimplemento__implemento'),
    cod_implemento = F('idprogramacionmantenimiento__idimplemento__codimplemento'),
    idimplemento = F('idprogramacionmantenimiento__idimplemento__idimplemento'),
  ).values(
    'idmantenimiento',
    'fecha_programada',
    'implemento',
    'cod_implemento',
    'idimplemento',
    'tipomantenimiento',
    'fechaingreso',
    'fechasalida',
    'descripcion',
    'persona',
    'fechaingreso',
    ))

  tareas = list(Acciones.objects.filter(estado = 0).values('idaccion','accion'))

  personas = list(Persona.objects.filter(estado = 1).values('idpersona', 'nombres', 'apellidos'))

  datos = {'mantenimientos': mantenimiento, 'tareas':tareas, 'personas':personas}
  return JsonResponse(datos)

def datos_implemento(request, id_implemento):
  pieza_implemento = list(DetImplementos.objects.filter(idimplemento = id_implemento).values())
  tareas_implemento = list(DetMotivos.objects.filter(idprogramacionmantenimiento = id_implemento).annotate(
    tarea= F('idaccion__accion'),
    idtarea= F('idaccion__idaccion')
  ).values('tarea', 'idtarea'))

  return JsonResponse({'partes': pieza_implemento, 'tareas':tareas_implemento})

def finalizar_mantenimiento(request, id_mantenimiento):
  if request.method == 'POST':
    encargado = request.POST.get('encargado')
    fecha_salida = request.POST.get('fecha-salida')
    tareas = request.POST.getlist('realizado')

    Mantenimiento.objects.filter(idmantenimiento = id_mantenimiento).update(
      persona_id= encargado,
      fechasalida = fecha_salida
    )

    for tarea in tareas:
      DetalleMantenimiento.objects.create(
        idmantenimiento_id = id_mantenimiento,
        idaccion_id = tarea
      )

      
    print(tareas)
  return redirect('mantenimiento_realizados')


def registrar_ingreso(request, id_mantenimiento):
  if request.method == 'POST':
    fecha_hoy =now()
    Mantenimiento.objects.filter(idmantenimiento = id_mantenimiento, estado = 1).update(fechaingreso= fecha_hoy)


  return redirect('programacion_mantenimiento')
    

def mantenimientos_realizados(request):
  return render(request, 'mantenimiento/completar_programaciones.html')
