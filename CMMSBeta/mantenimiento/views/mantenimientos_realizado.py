from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.timezone import now
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento, DetMotivos, Acciones, DetalleMantenimiento, Recambios
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.http import JsonResponse

@login_required(login_url='login', redirect_field_name='')
def datos_mantenimientos(request):
  mantenimiento = list(Mantenimiento.objects.filter(estado = 0).annotate(
  fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
  tipomantenimiento = F('idprogramacionmantenimiento__tipomantenimiento'),
  implemento = F('idprogramacionmantenimiento__idimplemento__idimplemento__implemento'),
  cod_implemento = F('idprogramacionmantenimiento__idimplemento__idimplemento__codimplemento'),
  idprogramacion = F('idprogramacionmantenimiento__idprogramacionmantenimiento'),
  idimplemento = F('idprogramacionmantenimiento__idimplemento__idimplemento__idimplemento'),
  nombres = F(f'idencargado__idpersona__nombres'),
  apellidos = F(f'idencargado__idpersona__apellidos')
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
    'idencargado',
    'nombres',
    'apellidos',
    'fechaingreso',
    'estado'
    ))


  datos = {'mantenimientos': mantenimiento}
  return JsonResponse(datos)

@login_required(login_url='login', redirect_field_name='')
def detalle_mantenimiento (request, id_mantenimiento):
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento__idmantenimiento = id_mantenimiento).annotate(
    tareas = F('idaccion__accion'),
  ).values('tareas','completado'))
  
  recambios = list(Recambios.objects.filter(idmantenimiento= id_mantenimiento).values())

  return JsonResponse({'tareas': tareas, 'recambios':recambios})

@login_required(login_url='login', redirect_field_name='')
def mantenimientos_realizados(request):
  rol = request.user.idrol.rol
  if rol == "Mecanico":
    return render(request, 'mantenimiento/mantenimientos_realizados.html')
  else:
    return redirect('home')

@login_required(login_url='login', redirect_field_name='')
def reporte_mantenimiento(request, id_mantenimiento):
  # Consultas 
  # Datos Mantenimietos
  mantenimiento = list(Mantenimiento.objects.filter(idmantenimiento = id_mantenimiento).annotate(
  fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
  tipomantenimiento = F('idprogramacionmantenimiento__tipomantenimiento'),
  implemento = F('idprogramacionmantenimiento__idimplemento__idimplemento__implemento'),
  cod_implemento = F('idprogramacionmantenimiento__idimplemento__idimplemento__codimplemento'),
  idprogramacion = F('idprogramacionmantenimiento__idprogramacionmantenimiento'),
  idimplemento = F('idprogramacionmantenimiento__idimplemento__idimplemento__idimplemento'),
  nombres = F(f'idencargado__idpersona__nombres'),
  apellidos = F(f'idencargado__idpersona__apellidos')
  ).values('idmantenimiento','idprogramacion','fecha_programada','implemento','cod_implemento',
           'idimplemento','tipomantenimiento','fechaingreso','fechasalida','descripcion','idencargado',
           'nombres','apellidos','fechaingreso','estado'
  ))
  # Datos Tareas y recambios
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento = id_mantenimiento).annotate(
  tareas = F('idaccion__accion'),
  ).values('tareas','completado'))
  
  recambios = list(Recambios.objects.filter(idmantenimiento= id_mantenimiento).values())

  # Definimos planatilla
  template = get_template('reportes/report_mantenimiento.html')
  context = {'titulo': 'Primer Pdf', 'mantenimiento':mantenimiento, 'tareas': tareas, 'recambios':recambios}
  html = template.render(context)
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="report.pdf"'

  # crear pdf
  pisa_status = pisa.CreatePDF(
      html, dest=response)
  
  # Controlar el error
  if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
  return response