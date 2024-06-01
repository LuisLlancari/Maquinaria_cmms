from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.timezone import now
from implemento.models import DetImplementos, Implemento
from usuario.models import Persona
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento, DetMotivos
from django.http import JsonResponse

def datos_mantenimiento(request):
  mantenimiento = list(Mantenimiento.objects.filter(fechaingreso__isnull=True, estado = 1).annotate(
    fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
    tipomantenimiento = F('idprogramacionmantenimiento__tipomantenimiento'),
    implemento = F('idprogramacionmantenimiento__idimplemento__implemento'),
    cod_implemento = F('idprogramacionmantenimiento__idimplemento__codimplemento'),
    idprogramacion = F('idprogramacionmantenimiento__idprogramacionmantenimiento'),
    idimplemento = F('idprogramacionmantenimiento__idimplemento__idimplemento'),
  ).values(
    'idmantenimiento',
    'idprogramacion',
    'fecha_programada',
    'implemento',
    'cod_implemento',
    'idimplemento',
    'tipomantenimiento',
    'fechaingreso',
    'estado'
    ))
  
  return JsonResponse({'mantenimiento':mantenimiento})

def registrar_ingreso(request, id_mantenimiento):
  if request.method == 'POST':
    fecha_hoy =now()
    # Mantenimiento.objects.filter(idmantenimiento = id_mantenimiento, estado = 1).update(fechaingreso= fecha_hoy)
    mantenimiento = get_object_or_404(Mantenimiento,idmantenimiento = id_mantenimiento, estado = 1)
    mantenimiento.fechaingreso= fecha_hoy
    mantenimiento.save()
    implemento = mantenimiento.idprogramacionmantenimiento.idimplemento.idimplemento
    Implemento.objects.filter(idimplemento = implemento).update(estado_actividad = 0)

  return redirect('mantenimiento_pendiente')



def mantenimiento_pendiente(request):
  return render(request, 'mantenimiento/iniciar_mantenimiento.html')
