from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F, Value
from django.db.models.functions import Concat
from operarios.models import Encargado
from implemento.models import DetImplementos, Implemento
from componente_pieza.models import DetalleConfiguracion
from usuario.models import Persona
from mantenimiento.models import Mantenimiento, DetMotivos, Acciones, DetalleMantenimiento, Recambios, ProgramacionMantenimiento
from django.http import JsonResponse

@login_required(login_url='login', redirect_field_name='')
def datos_mantenimiento(request):
  mantenimiento = list(Mantenimiento.objects.filter(fechaingreso__isnull=False, fechasalida__isnull=True, estado = 1).annotate(
    fecha_programada = F('idprogramacionmantenimiento__fechaprogramacion'),
    tipomantenimiento = F('idprogramacionmantenimiento__tipomantenimiento'),
    implemento = F('idprogramacionmantenimiento__idimplemento__implemento'),
    cod_implemento = F('idprogramacionmantenimiento__idimplemento__codimplemento'),
    idprogramacion = F('idprogramacionmantenimiento__idprogramacionmantenimiento'),
    idimplemento = F('idprogramacionmantenimiento__idimplemento__idimplemento'),
    nombres = F('idencargado__idpersona__nombres'),
    apellidos = F('idencargado__idpersona__nombres')
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

  tareas = list(Acciones.objects.filter(estado = 0).values('idaccion','accion'))

  encargados = list(Encargado.objects.filter(estado = 1).annotate(
    nombre =Concat(F('idpersona__nombres'),Value(' '), F('idpersona__apellidos')) 
  ).values('idencargado', 'nombre'))

  
  datos = {'mantenimientos': mantenimiento, 'tareas':tareas, 'encargados':encargados}
  return JsonResponse(datos)

@login_required(login_url='login', redirect_field_name='')
def datos_implemento(request, id_programacion, id_implemento):
  tareas_implemento = list(DetMotivos.objects.filter(idprogramacionmantenimiento = id_programacion).annotate(
    tarea= F('idaccion__accion'),
    idtarea= F('idaccion__idaccion')
  ).values('tarea', 'idtarea'))

  detalle_pieza = list(DetImplementos.objects.filter(idimplemento = id_implemento).annotate(
      pieza=Concat(
        F('iddetallecomponente__idpieza__pieza'),
        Value(' - '),
        F('iddetallecomponente__idpieza__codpieza'),
        ),
      codigo = F('iddetallecomponente__idpieza__codpieza')
  ).values(
    'pieza',
    'codigo'
  ))

  implemento = get_object_or_404(Implemento, idimplemento =id_implemento)

  id_configuracion = implemento.idtipoimplemento.idconfiguracion_implemento.idconfiguraciontipoimplemento

  detalle_componente = list(DetalleConfiguracion.objects.filter(idconfiguracion = id_configuracion).annotate(
      componente=Concat(
        F('idcomponente__componente'),
        Value(' - '),
        F('idcomponente__codcomponente'),
      ),
      codigo = F('idcomponente__codcomponente')
  ).values(
    'componente',
    'codigo'
  ))

  partes ={
    'componentes': detalle_componente,
    'pieza': detalle_pieza
  }

  return JsonResponse({'partes': partes, 'tareas':tareas_implemento})

@login_required(login_url='login', redirect_field_name='')
def finalizar_mantenimiento(request, id_mantenimiento):
  if request.method == 'POST':
    # Obtenemos los datos del request
    encargado = request.POST.get('encargado')
    fecha_salida = request.POST.get('fecha-salida')
    tareas_realizadas = request.POST.getlist('realizado')
    tareas_asignadas = request.POST.getlist('tareas_asignadas')
    recambios = request.POST.getlist('recambios')


    # Creamos Detalle Mantenimiento
    for asignada in tareas_asignadas:
      if asignada in tareas_realizadas:
        # Instanciamos las foraneas
        accion = get_object_or_404(Acciones, accion = asignada)
        mantenimiento = get_object_or_404(Mantenimiento,idmantenimiento = id_mantenimiento)
        # Creamos el registro
        DetalleMantenimiento.objects.create(
          idaccion = accion,
          idmantenimiento = mantenimiento,
          completado = True,
        )
      else:
        # Instanciamos las foraneas
        accion = get_object_or_404(Acciones, accion = asignada)
        mantenimiento = get_object_or_404(Mantenimiento,idmantenimiento = id_mantenimiento)
        # Creamos el registro
        DetalleMantenimiento.objects.create(
          idaccion = accion,
          idmantenimiento = mantenimiento,
          completado = False,
        )

    # Creamos Detelle de Recambios
    if len(recambios) > 0:
      for item in recambios:
        # Extraemos el codigo
        partes = item.split(" - ")
        item = partes[0]
        codigo = partes[1]
        # Creamos recambios
        Recambios.objects.create(
          idmantenimiento_id = id_mantenimiento,
          item = item,
          codigo = codigo,
      )   
    else:
      pass

    # print(f'Recambios :{recambios}')
    # Colocamos fecha de salida y encargado al registro de mantenimiento
    mantenimiento = get_object_or_404(Mantenimiento,idmantenimiento = id_mantenimiento)
    mantenimiento.idencargado_id = encargado
    mantenimiento.fechasalida = fecha_salida
    mantenimiento.estado = 0
    mantenimiento.save()

    programacion = mantenimiento.idprogramacionmantenimiento.idprogramacionmantenimiento
    ProgramacionMantenimiento.objects.filter(idprogramacionmantenimiento = programacion).update(estado_mantenimiento = 2)
    # activamos el implemento 
    implemento =mantenimiento.idprogramacionmantenimiento.idimplemento.idimplemento
    frecuencia_mantenimiento =mantenimiento.idprogramacionmantenimiento.idimplemento.idtipoimplemento.frecuencia_man
    proximo_mantenimiento = mantenimiento.idprogramacionmantenimiento.idimplemento.proximo_mantenimiento
    nuevo_mantenimiento = proximo_mantenimiento + frecuencia_mantenimiento
    
    Implemento.objects.filter(idimplemento = implemento).update(estado_actividad = 1, proximo_mantenimiento = nuevo_mantenimiento ) 
    
  return redirect('mantenimiento_proceso')

@login_required(login_url='login', redirect_field_name='')
def detalle_mantenimiento (request, id_mantenimiento):
  tareas = list(DetalleMantenimiento.objects.filter(idmantenimiento = id_mantenimiento).annotate(
    tareas = F('idaccion__accion'),
  ).values(
    'tareas',
    'completado'))
  

  return JsonResponse({'tareas': tareas})

@login_required(login_url='login', redirect_field_name='')
def mantenimiento_proceso(request):
  rol = request.user.idrol.rol
  if rol == "Mecanico":
    return render(request, 'mantenimiento/completar_mantenimiento.html')
  else:
    return redirect('home')
