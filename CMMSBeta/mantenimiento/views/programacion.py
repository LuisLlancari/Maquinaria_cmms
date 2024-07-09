from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento, DetalleMantenimiento, Recambios
from django.http import JsonResponse
from implemento.models import Implemento, TipoImplemento, DetImplementos, ImplementoSupervisor
from mantenimiento.models import Acciones, DetMotivos
from django.contrib import messages
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.http import JsonResponse

# funcion que calculara las fechas de mantenimiento
@login_required(login_url='login', redirect_field_name='')
def programacion_mantenimiento(request):
    usuario_id = request.user.id
    rol = request.user.idrol.rol
    if rol == "Supervisor":

        datos = ProgramacionMantenimiento.objects.filter(idimplemento__idsupervisor = usuario_id).order_by('-fechaprogramacion')
        acciones = Acciones.objects.filter(estado__in=[0, 2], estado_actividad = True)
        implementos = ImplementoSupervisor.objects.filter(estado = True, idsupervisor = usuario_id)
        tipoimplementos = TipoImplemento.objects.filter(estado = True)
        contexto = {
            'datos': datos,
            'acciones': acciones,
            'implementos': implementos,
            'tipoimplementos': tipoimplementos
        }    
        return render(request, 'mantenimiento/programacion.html', contexto)
    else:
        return redirect('home')
        
@login_required(login_url='login', redirect_field_name='')
def registrar_fecha(request, id_implemento):
    if request.method == 'POST':
        fecha = request.POST.get('fecha_programacion')
        motivos = request.POST.getlist('idmotivo')
       
       # Actualizar Programacion con un save
        programacion = get_object_or_404(ProgramacionMantenimiento, idprogramacionmantenimiento=id_implemento, estado=1)
        programacion.fechaprogramacion = fecha
        programacion.save()

        for idmotivo in motivos:
            if DetMotivos.objects.filter(idprogramacionmantenimiento_id = id_implemento, idaccion_id = idmotivo).exists():
                motivo = Acciones.objects.get(pk = idmotivo)
                messages.error(request, f"El motivo {motivo} ya registrado", extra_tags='danger')
            else:
                DetMotivos.objects.create(idprogramacionmantenimiento_id = id_implemento, idaccion_id = idmotivo)

    return redirect('programacion_mantenimiento')

@login_required(login_url='login', redirect_field_name='')
def registrar(request):
    if request.method == 'POST':
        implemento = request.POST.get('idimplemento')
        fecha = request.POST.get('fecha_programacion')
        motivos = request.POST.getlist('idmotivo')
        # tipo_mantnimiento = 0 : Correctivo
        buscarprogramacion = ProgramacionMantenimiento.objects.filter(idimplemento_id = implemento, tipomantenimiento = 0, estado_mantenimiento = 0, estado = 1).exists()
        programacion = ProgramacionMantenimiento.objects.filter(idimplemento_id = implemento, tipomantenimiento = 0, estado_mantenimiento = 1, estado = 1).exists()
        
        #true
        #print(buscarmantenimiento) 
        if buscarprogramacion == True:
            messages.error(request, 'La el implemetento ya se encuentra programado', extra_tags='danger')
            return redirect('programacion_mantenimiento')     
        elif programacion == True:
            messages.error(request, 'La el implemetento ya esta en un mantenimiento', extra_tags='danger')
            return redirect('programacion_mantenimiento')
        else:
            nueva_programacion =  ProgramacionMantenimiento.objects.create(idimplemento_id = implemento, fechaprogramacion = fecha, tipomantenimiento = 0)

            for idmotivo in motivos:
                if DetMotivos.objects.filter(idprogramacionmantenimiento_id = nueva_programacion.idprogramacionmantenimiento, idaccion_id = idmotivo).exists():
                    motivo = Acciones.objects.get(pk = idmotivo)
                    messages.error(request, f"El motivo {motivo} ya registrado", extra_tags='danger')
                else:
                    DetMotivos.objects.create(idprogramacionmantenimiento_id = nueva_programacion.idprogramacionmantenimiento, idaccion_id = idmotivo)
            messages.success(request, 'La programación se ha creado exitosamente', extra_tags='success')

    return redirect('programacion_mantenimiento')

@login_required(login_url='login', redirect_field_name='')
def eliminar_programacion(request, id_programacion):
    programacion = get_object_or_404(ProgramacionMantenimiento, pk=id_programacion)
    if request.method == 'POST':
        aceptado = ProgramacionMantenimiento.objects.filter(idprogramacionmantenimiento = id_programacion, estado_mantenimiento = 1).exists()
        # Si es True, Sale una alerta , si es False elimina la programación
        if aceptado == False:
            #print(id_programacion)
            # Encuentra todos los mantenimientos asociados a la programación
            mantenimiento = Mantenimiento.objects.filter(idprogramacionmantenimiento_id=id_programacion)
            mantenimiento.delete()
            # Elimina cualquier registro dependiente de los mantenimientos, si existe alguna tabla relacionada, ej. MantenimientoDetMotivos
            DetMotivos.objects.filter(idprogramacionmantenimiento_id= id_programacion).delete()
            # Finalmente, elimina la programación
            programacion.delete()
        else:
            messages.error(request, 'La programación se encuentra aceptada, no puede ser eliminada.', extra_tags='danger')

    return redirect('programacion_mantenimiento')

@login_required(login_url='login', redirect_field_name='')
def editar_fecha(request):
    if request.method == 'POST':
        
        idprogramacion = request.POST.get('idprogramacion')
        aceptado = ProgramacionMantenimiento.objects.filter(idprogramacionmantenimiento = idprogramacion, estado_mantenimiento = 1).exists()
        if aceptado == False:
            fecha = request.POST.get('fechaprogramacion')
            programacion = get_object_or_404(ProgramacionMantenimiento, pk = idprogramacion)
            programacion.fechaprogramacion = fecha
            programacion.save()
        else:
            messages.error(request, 'La programación se encuentra aceptada, no puede ser editada.', extra_tags='danger')
    return redirect('programacion_mantenimiento')

@login_required(login_url='login', redirect_field_name='')
def datos_mantenimiento(request, id_programacion):

  id = get_object_or_404(Mantenimiento, idprogramacionmantenimiento_id = id_programacion)

  mantenimiento = list(Mantenimiento.objects.filter(estado = 0, idprogramacionmantenimiento_id = id_programacion).annotate(
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
  
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento = id.idmantenimiento).annotate(
    tareas = F('idaccion__accion'),
  ).values(
    'tareas',
    'completado'))
  
  recambios = list(Recambios.objects.filter(idmantenimiento= id.idmantenimiento).values())

  datos = {
      'mantenimientos': mantenimiento,
      'tareas': tareas,
      'recambios': recambios
      }
  return JsonResponse(datos)

@login_required(login_url='login', redirect_field_name='')
def reporte_mantenimiento(request, id_programacion):
  # Consultas 
  # Datos Mantenimietos
  id = get_object_or_404(Mantenimiento, idprogramacionmantenimiento_id = id_programacion)

  mantenimiento = list(Mantenimiento.objects.filter(idprogramacionmantenimiento_id = id_programacion).annotate(
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
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento = id.idmantenimiento).annotate(
  tareas = F('idaccion__accion'),
  ).values('tareas','completado'))
  
  recambios = list(Recambios.objects.filter(idmantenimiento= id.idmantenimiento).values())

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