from django.shortcuts import render
from programacion_labor.models import Programacion, DetalleLabor
from tractor.models import Tractor
from operarios.models import Solicitante
from django.contrib.auth.decorators import login_required
from usuario.models import * 
from django.http import JsonResponse
from django.db.models import Count, Subquery
from programacion_labor.models import *
from implemento.models import *
from django.core.paginator import Paginator


@login_required(login_url='login', redirect_field_name='home')
def home(request,):

    usuario = request.user
    usuarios = Usuario.objects.filter(idrol = 1)
    tipos_labor = Programacion.objects.values('idtipolabor', 'idtipolabor__tipolabor').distinct()
    
    data = {
        'user': usuario,
        'usuarios': usuarios,
        'tipolabor': tipos_labor,
    }
   
    return render(request, 'core/home.html', data)

def datos_grafico(request, fecha, supervisor, turnos):
 
    # Consulta para encontrar los tractores que pertenecen al supervisor y no estuvieron programados
    tractores_no_programados = Tractor.objects.filter(
        idusuario=supervisor
    ).exclude(
        programacion__fechahora=fecha,
        programacion__turno=turnos
    )

    # Contar el número de tractores no programados
    num_tractores_no_programados = tractores_no_programados.count()

    # Crear un diccionario para almacenar los resultados de los tractores no programados
    resultado_tractores = {
        'nombre': 'Tractores no programados',
        'registros': num_tractores_no_programados
    }

    # Consulta para contar la cantidad de registros de cada solicitante
    registros_por_solicitante = Programacion.objects.filter(
        fechahora=fecha,
        turno=turnos,
        idusuario = supervisor,
        idtractor__idusuario =supervisor
    ).values('idsolicitante').annotate(num_registros=Count('idsolicitante'))

    # Crear una lista para almacenar los resultados de los solicitantes
    resultados_solicitantes = []

    # Agregar el resultado de los tractores no programados como el primer elemento de la lista
    resultados_solicitantes.append(resultado_tractores)

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

    # Obtener todos los solicitantes y agregar aquellos que no tienen registros como 0
    todos_solicitantes = Solicitante.objects.all()
    for solicitante in todos_solicitantes:
        nombre_solicitante = f"{solicitante.idpersona.nombres} {solicitante.idpersona.apellidos}"

    # Devolver los resultados como una respuesta JSON
    return JsonResponse({
        'resultados_solicitantes': resultados_solicitantes
    })

def datos_tabla(request, fecha, supervisor, turno):
    # Obtener todos los tractores relacionados con el supervisor
    tractores_usuario = Tractor.objects.filter(idusuario=supervisor)

    # Obtener los fundos de tractores y contar cuántos tractores hay en cada fundo
    info_fundos = tractores_usuario.values('idfundo__fundo', 'idfundo').annotate(total_tractores=Count('idfundo'))
    print(info_fundos)

    # Obtener los tractores programados en la fecha y turno especificados en los fundos relacionados al usuario
    tractores_programados = Programacion.objects.filter(idtractor__idusuario=supervisor, fechahora=fecha, turno=turno).values('idtractor__idfundo__fundo').annotate(total_tractores_programados=Count('idtractor'))

    # Colocamos la informacion en la lista
    resultado = []
    for fundo_info in info_fundos:
        fundo_nombre = fundo_info['idfundo__fundo']
        idfundo = fundo_info['idfundo']
        total_tractores = fundo_info['total_tractores']
        tractores_programados_en_fundo = next((tp['total_tractores_programados'] for tp in tractores_programados if tp['idtractor__idfundo__fundo'] == fundo_nombre), 0)
        tractores_sin_programar_en_fundo = total_tractores - tractores_programados_en_fundo
        resultado.append({
            'Fundo': fundo_nombre,
            'idfundo': idfundo,
            'tractores_totales': total_tractores,
            'tractores_programados': tractores_programados_en_fundo,
            'tractores_sin_programar': tractores_sin_programar_en_fundo
        })

    return JsonResponse({'tabla_tractor': resultado})
    
def datos_tabla_detalle(request, fecha, supervisor, turno, idfundo):
    tractores_sin_programacion = list(Tractor.objects.filter(
        idusuario=supervisor,
        idfundo=idfundo
    ).exclude(
        idtractor__in=Subquery(Programacion.objects.filter(
            fechahora=fecha,
            turno=turno,
            idtractor__idusuario=supervisor,
            idtractor__idfundo_id=idfundo
        ).values('idtractor'))
    ).values('nrotractor'))


    # Obtenemos los implementos utilizados
    detprogramaciones = DetalleLabor.objects.filter(
        idprogramacion__fechahora= fecha,
        idprogramacion__turno= turno,
        idprogramacion__idtractor__idusuario_id = supervisor,
        idprogramacion__idtractor__idfundo_id = idfundo
    ).values(
        'idimplemento__implemento',
        'idimplemento__idimplemento'
    )
    detprogramacione_list=[]

    for detprogramacion in detprogramaciones:
        implemento = detprogramacion['idimplemento__implemento']
        detprogramacione_list.append({
            'implemento_usado' : implemento     
        })

    # Obtenemos la informacion de los tractores que tuvieron una programacion
    programaciones = Programacion.objects.filter(
        fechahora=fecha,
        turno=turno,
        idtractor__idusuario=supervisor,
        idtractor__idfundo_id=idfundo
    ).values(
        'idtractor__idtractor', 
        'idprogramacion',
        'idtractor__nrotractor', 
        'idtipolabor__tipolabor',
        'idsolicitante__idpersona__nombres',
        'idsolicitante__idpersona__apellidos')

    programaciones_list = []
    for programacion in programaciones:
        nombre_tractor = programacion['idtractor__nrotractor']
        labor_tractor = programacion['idtipolabor__tipolabor']
        nombre_solicitante = f"{programacion['idsolicitante__idpersona__nombres']} {programacion['idsolicitante__idpersona__apellidos']}"
        programaciones_list.append({
            'tractor': nombre_tractor,
            'labor': labor_tractor,
            'solicitante': nombre_solicitante,
            'implementos':detprogramacione_list
        })   
        

    return JsonResponse({'programaciones':programaciones_list, 'tractores_sin_programacion': tractores_sin_programacion})

@login_required(login_url='login', redirect_field_name='home')
def test(request):
    #
    lista_detalle = DetalleLabor.objects.all().order_by('-idprogramacion__fechahora')
    #paginator = Paginator(lista_detalle, 10)  # Muestra 10 elementos por página
    page_number = request.GET.get('page')
    #paginador
    #page_obj = paginator.get_page(page_number)

    lista_implementos = Implemento.objects.all()
    #
    lista_supervisor = Usuario.objects.filter(idrol = 3)

    context = {
        'detlabor': lista_detalle,  # Pasar el objeto de la página a la plantilla
        'imple': lista_implementos,
        'list_sup': lista_supervisor
    }
    return render(request, 'core/test.html', context)





















