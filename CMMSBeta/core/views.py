from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Subquery, F,Value, OuterRef
from django.db.models.functions import Concat
from programacion_labor.models import Programacion, DetalleLabor
from tractor.models import Tractor
from operarios.models import Solicitante
from usuario.models import * 
from django.http import JsonResponse
from programacion_labor.models import *
from implemento.models import *
from django.core.paginator import Paginator


@login_required(login_url='login', redirect_field_name='home')
def home(request,):
    rol_usuario = request.user.idrol.rol
    if rol_usuario == "Supervisor":
        return redirect('implemento')
    elif rol_usuario == "Mecanico":
        return redirect('mantenimiento_pendiente')
    elif rol_usuario == "Asistente":
        return redirect('reportetractor')
    else:
        usuario = request.user
        usuarios = Usuario.objects.filter(idrol = 3, is_active = 1)
        tipos_labor = Programacion.objects.values('idtipolabor', 'idtipolabor__tipolabor')

        data = {
            'user': usuario,
            'usuarios': usuarios,
            'tipolabor': tipos_labor,
        }
        return render(request, 'core/home.html', data)
    
@login_required(login_url='login', redirect_field_name='')
def datos_grafico(request, fecha, supervisor, turnos):
    # Definir los filtros comunes
    filtro_tractores = {'estado': True}
    filtro_programacion = {'fechahora': fecha, 'turno': turnos, 'idtractor__estado': True}

    if supervisor != 0:
        filtro_tractores['idsupervisor'] = supervisor
        filtro_programacion.update({'idusuario': supervisor, 'idtractor__idtractor__idusuario': supervisor})

    # Consulta para encontrar los tractores que no estuvieron programados
    tractores_no_programados = TractorSupervisor.objects.filter(**filtro_tractores).exclude(
        programacion__fechahora=fecha,
        programacion__turno=turnos
    )

    # Contar el número de tractores no programados
    num_tractores_no_programados = tractores_no_programados.count()

    # Crear un diccionario para almacenar los resultados de tractores
    resultado_tractores = {
        'nombre': 'Tractores no programados',
        'registros': num_tractores_no_programados
    }

    # Consulta para contar la cantidad de registros de cada solicitante
    registros_por_solicitante = Programacion.objects.filter(**filtro_programacion).values('idsolicitante').annotate(num_registros=Count('idsolicitante'))

    # Lista para almacenar datos
    resultados_solicitantes = [resultado_tractores]

    # Agregar los resultados de los solicitantes a la lista
    for registro in registros_por_solicitante:
        solicitante_id = registro['idsolicitante']
        num_registros = registro['num_registros']
        solicitante = Solicitante.objects.get(idsolicitante=solicitante_id)
        nombre_solicitante = f"{solicitante.idpersona.nombres} {solicitante.idpersona.apellidos}"
        resultado = {
            'nombre': nombre_solicitante,
            'registros': num_registros
        }
        resultados_solicitantes.append(resultado)

    # Obtener todos los solicitantes 
    todos_solicitantes = Solicitante.objects.all()
    for solicitante in todos_solicitantes:
        nombre_solicitante = f"{solicitante.idpersona.nombres} {solicitante.idpersona.apellidos}"

    # Retornar en JSON
    return JsonResponse({
        'resultados_solicitantes': resultados_solicitantes
    })

@login_required(login_url='login', redirect_field_name='')
def datos_tabla(request, fecha, supervisor, turno):
  # Definir el filtro para tractores
    filtro_tractores = {'estado': True}
    filtro_programacion = {'fechahora': fecha, 'turno': turno, 'idtractor__estado': True}

    if supervisor != 0:
        filtro_tractores['idsupervisor'] = supervisor
        filtro_tractores['estado'] = True
        filtro_programacion['idtractor__idsupervisor'] = supervisor

    # Obtener todos los tractores relacionados con el supervisor
    tractores_usuario = TractorSupervisor.objects.filter(**filtro_tractores)

    # Obtener los fundos de tractores y contar cuántos tractores hay en cada fundo
    info_fundos = tractores_usuario.values('idtractor__idfundo__fundo', 'idtractor__idfundo').annotate(total_tractores=Count('idtractor__idfundo'))

    # Obtener los tractores programados en la fecha y turno especificados en los fundos relacionados al usuario
    tractores_programados = Programacion.objects.filter(**filtro_programacion).values('idtractor__idtractor__idfundo__fundo').annotate(total_tractores_programados=Count('idtractor')).values()

    # Depuración: imprimir los resultados de tractores programados
    print("tractores_programados:", list(tractores_programados))

    # Colocar la información en la lista
    resultado = []
    for fundo_info in info_fundos:
        fundo_nombre = fundo_info['idtractor__idfundo__fundo']
        idfundo = fundo_info['idtractor__idfundo']
        total_tractores = fundo_info['total_tractores']
        tractores_programados_en_fundo = next((tp['total_tractores_programados'] for tp in tractores_programados if tp.get('idtractor__idtractor__idfundo__fundo') == fundo_nombre), 0)
        tractores_sin_programar_en_fundo = total_tractores - tractores_programados_en_fundo
        resultado.append({
            'Fundo': fundo_nombre,
            'idfundo': idfundo,
            'tractores_totales': total_tractores,
            'tractores_programados': tractores_programados_en_fundo,
            'tractores_sin_programar': tractores_sin_programar_en_fundo
        })

    return JsonResponse({'tabla_tractor': resultado})

@login_required(login_url='login', redirect_field_name='')
def datos_tabla_detalle(request, fecha, supervisor, turno, idfundo):
   # Definir los filtros comunes
    filtro_tractores = {'idtractor__idfundo': idfundo, 'estado': True}
    filtro_programacion = {
        'fechahora': fecha,
        'turno': turno,
        'idtractor__idtractor__idfundo': idfundo,
        'idtractor__idtractor__estado': True  # Asegurar que sólo tractores activos sean considerados
    }
    filtro_detprogramaciones = {
        'idprogramacion__fechahora': fecha,
        'idprogramacion__turno': turno,
        'idprogramacion__idtractor__idtractor__idfundo': idfundo,
        'idprogramacion__idtractor__idtractor__estado': True  # Asegurar que sólo tractores activos sean considerados
    }

    if supervisor != 0:
        filtro_tractores['idsupervisor'] = supervisor
        filtro_programacion['idtractor__idsupervisor'] = supervisor
        filtro_detprogramaciones['idprogramacion__idtractor__idsupervisor'] = supervisor

    # Tractores no Asignados
    tractores_programados = Programacion.objects.filter(**filtro_programacion).values('idtractor')
    tractores_sin_programacion = list(
        TractorSupervisor.objects.filter(**filtro_tractores).exclude(
            idtractorsupervisor__in=tractores_programados
        ).values('idtractor__nrotractor')
    )

    # Obtener la información de los tractores que tuvieron una programación
    programaciones = Programacion.objects.filter(**filtro_programacion).annotate(
        id_tractor=F('idtractor__idtractor__idtractor'),
        tractor=F('idtractor__idtractor__nrotractor'),
        labor=F('idtipolabor__tipolabor'),
        solicitante=Concat(F('idsolicitante__idpersona__nombres'), Value(' '), F('idsolicitante__idpersona__apellidos'))
    ).values(
        'id_tractor',
        'idprogramacion',
        'tractor',
        'labor',
        'solicitante'
    )

    # Recorremos las programaciones para obtener los implementos utilizados por cada programación
    programaciones_list = []
    for programacion in programaciones:
        id_programacion = programacion['idprogramacion']
        tractor = programacion['tractor']
        labor = programacion['labor']
        solicitante = programacion['solicitante']

        # Obtenemos los implementos utilizados
        detprogramaciones = DetalleLabor.objects.filter(
            idprogramacion=id_programacion,
            **filtro_detprogramaciones
        ).annotate(
            implemento=F('idimplemento__idimplemento__implemento'),
            id_implemento=F('idimplemento__idimplemento__idimplemento')
        ).values(
            'id_implemento',
            'implemento'
        )

        # Creamos una lista de los implementos
        datos_implementos = [{'implemento': detalle['implemento']} for detalle in detprogramaciones]

        # Añadimos los datos
        datos = {
            'programacion': id_programacion,
            'tractor': tractor,
            'labor': labor,
            'solicitante': solicitante,
            'implementos': datos_implementos
        }
        programaciones_list.append(datos)

    return JsonResponse({'programaciones': programaciones_list, 'tractores_sin_programacion': tractores_sin_programacion})

@login_required(login_url='login', redirect_field_name='home')
def test(request):
    #
    subquery = DetalleLabor.objects.filter(
    estado=True,
    idprogramacion=OuterRef('idprogramacion')
    ).order_by('idprogramacion__fechahora')[:1]

    # Obtener los detalles únicos por idprogramacion y ordenarlos de forma ascendente por la fecha de idprogramacion
    detalles_unicos = DetalleLabor.objects.filter(
        pk=Subquery(subquery.values('pk'))
    ).order_by('-idprogramacion__fechahora')

    print(detalles_unicos)

    lista_implementos = Implemento.objects.all()
    lista_supervisor = Usuario.objects.filter(idrol = 3, is_active = 1)

    context = {
        'detlabor': detalles_unicos,  # Pasar el objeto de la página a la plantilla
        'imple': lista_implementos,
        'list_sup': lista_supervisor
    }
    return render(request, 'core/test.html', context)





















