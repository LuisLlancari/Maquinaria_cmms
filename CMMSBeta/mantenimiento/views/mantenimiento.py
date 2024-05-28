from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.timezone import now
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento
from django.http import JsonResponse

def datos_mantenimiento(request):
  matenimiento = Mantenimiento.objects.filter(estado = 1).annotate(
    fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
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
    )
  mantenimiento = list(matenimiento)
  return JsonResponse({'mantenimientos':mantenimiento})
  # return render(request, 'mantenimiento/completar_programaciones.html')

def registrar_ingreso(request, id_mantenimiento):
  if request.method == 'POST':
    fecha_hoy =now()
    Mantenimiento.objects.filter(idmantenimiento = id_mantenimiento, estado = 1).update(fechaingreso= fecha_hoy)


  return redirect('programacion_mantenimiento')
    

def mantenimientos_realizados(request):
  return render(request, 'mantenimiento/completar_programaciones.html')
