from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.db.models import F
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max , Count, Subquery, OuterRef
from implemento.models import *
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from implemento.models import *
from usuario.models import *
from operarios.models import *
from tractor.models import *
from fundo_cultivo.models import *
from django.contrib.auth.decorators import login_required
from datetime import timedelta

#Programacion 
@login_required(login_url='login', redirect_field_name='')
def programacion(request):
    rol = request.user.idrol.rol
    if rol == "Supervisor":
        # Formateo de la fecha - Peru
        ahora_utc = timezone.now()
        ahora_peru = ahora_utc - timedelta(hours=5)
        hoy = ahora_peru.date()
            #Uso del Formateo
        cantidad_tractores_hoy = Programacion.objects.filter(fechahora=hoy, idusuario = request.user).count()
        # Fin Formateo de la fecha

        #Obtenemos el idusuario
        usuario_id = request.user.id

        #tractoristas = Tractorista.objects.filter(estado = True, estado_actividad = True)
        #tractor = Tractor.objects.filter(estado = True, estado_actividad = True)
        #implementos = Implemento.objects.filter(estado = True, estado_actividad = True)

        fundos = Fundo.objects.filter(estado = True)
        lotes = Lote.objects.filter(estado = True)
        detalles = DetalleLabor.objects.filter(estado = True, idprogramacion__idusuario = usuario_id)

        #Obtenemos detalles unicos
        subquery = DetalleLabor.objects.filter(
        estado=True,
        idprogramacion=OuterRef('idprogramacion'),
        idprogramacion__idusuario=usuario_id
        ).order_by('idprogramacion__fechahora')[:1]

        # Obtener los detalles únicos por idprogramacion y ordenarlos de forma ascendente por la fecha de idprogramacion
        detalles_unicos = DetalleLabor.objects.filter(
            pk=Subquery(subquery.values('pk'))
        ).order_by('-idprogramacion__fechahora')

        #LISTA DE USUARIO PARA EL SELECT 
        usuario = Usuario.objects.filter(idrol = 3, is_active = 1)

        # Pasamos los datos al contexto
        contexto = {
            'cantidad'          : cantidad_tractores_hoy ,
            'fecha'             : hoy, 
            'detalle'           : detalles_unicos, 
            'idusuario'         : usuario_id, 
            'lista_usuarios'    : usuario ,
            'fundo'             : fundos,
            'lotes'             : lotes,
            'form_programacion' : ProgramacionForm, 
        }


        return render(request, 'programacion_labor/programacion.html', contexto)
    else:
        return redirect('home')

@login_required(login_url='login', redirect_field_name='')
def registrar_programacion(request):
    if request.method == 'POST':
        form = ProgramacionForm(request.POST)
        if form.is_valid():
            try:
                idtractor = form.cleaned_data['idtractor']
                # idtractorista = form.cleaned_data['idtractorista']
                idtractorista = request.POST.get('idtractorista')

                programacion = form.save()

                # Obtener el ID de la última programación guardada
                ultimo_id = Programacion.objects.aggregate(Max('idprogramacion'))['idprogramacion__max']

                # Obtener los implementos seleccionados del formulario
                implementos_seleccionados = request.POST.getlist('idimplemento')
                print("implementos:")
                print(implementos_seleccionados)

                # Crear un detalle de labor para cada implemento seleccionado
                for implemento_id in implementos_seleccionados:
                    if DetalleLabor.objects.filter(idprogramacion=programacion, idimplemento_id=implemento_id).exists():
                        implemento = ImplementoSupervisor.objects.get(pk=implemento_id)
                        messages.error(
                            request,
                            f'El implemento {implemento.idimplemento.implemento} ya se encuentra registrado en esta programación.',
                            extra_tags='danger'
                        )
                    else:
                        implemento = ImplementoSupervisor.objects.get(pk=implemento_id)
                        DetalleLabor.objects.create(idprogramacion=programacion, idimplemento=implemento, horadeuso=0)


                #Tractor.objects.filter(nrotractor=idtractor).update(estado_actividad=False)
                # Tractorista.objects.filter(pk=idtractorista).update(estado_actividad=False)

                messages.success(request, "La programación ha sido agregada correctamente", extra_tags='success')
                return redirect('programacion')
            except Exception as e:
                messages.error(request, f"Error al registrar la programación: {e}", extra_tags='danger')
                return redirect('programacion')
        else:
            # print(form.errors)
            messages.error(request, f"Errores en el formulario: {form.errors}", extra_tags='danger')
            return redirect('programacion')

@login_required(login_url='login', redirect_field_name='')
def eliminar_programacion(request, id_programacion):
    det = DetalleLabor.objects.filter(idprogramacion=id_programacion)
    prog = Programacion.objects.filter(idprogramacion=id_programacion)
    print(det)
    print(prog)
    if request.method == 'POST':
        if prog[0].estado == 1:
            det.delete()
            prog.delete()
            messages.success(request, "La programación ha sido eliminada correctamente", extra_tags='success')
            return redirect('programacion')
        else:
            messages.error(request, "La programación ya se confirmo", extra_tags='danger')
            return redirect('programacion')

    return redirect('programacion')

@login_required(login_url='login', redirect_field_name='')
def obtener_data(request, id_programacion):
    detalles_labor = DetalleLabor.objects.filter(idprogramacion=id_programacion)
    nombres_implementos = []
    for detalle_labor in detalles_labor:
        nombres_implementos.append(detalle_labor.idimplemento.implemento)  # Nombre del implemento
    if nombres_implementos:
        data = {'mensaje': "Success", 'nombres_implementos': nombres_implementos}
    else:
        data = {'mensaje': "Not found"}
    return JsonResponse(data)


@login_required(login_url='login', redirect_field_name='')
def obtener_select(request, fecha, turno):
    # Obtener los ids de tractoristas de las programaciones según fecha y turno
    list_tractorista = list(Programacion.objects.filter(fechahora=fecha, turno=turno).values_list('idtractorista_id', flat=True))
    list_tractores = list(Programacion.objects.filter(fechahora=fecha, turno=turno).values_list('idtractor_id', flat=True))

    # Para obtener los implemenos , hacemos una jugada ganadora
    list_programaciones = list(Programacion.objects.filter(fechahora=fecha, turno=turno))
    list_implementos = list(DetalleLabor.objects.filter(idprogramacion__in=list_programaciones).values_list('idimplemento_id', flat=True))

    # Excluir los todo lo ingresado con los ids obtenidos
    tractoristas = Tractorista.objects.filter(estado = True).exclude(idtractorista__in=list_tractorista)
    # Tractores
    tractores = Tractor.objects.filter(estado = True).exclude(idtractor__in=list_tractores).values()
    tractores2 = TractorSupervisor.objects.filter(estado = True).exclude(idtractorsupervisor__in=list_tractores).annotate(
        idusuario =F('idsupervisor'),
        idusuario_id =F('idsupervisor__idusuario'),
        idfundo =F('idtractor__idfundo'),
        nrotractor = F('idtractor__nrotractor')
    ).values('idusuario', 'idusuario_id', 'idtractor', 'nrotractor', 'idfundo', 'idtractorsupervisor')
    # Implementos
    implementos = Implemento.objects.filter(estado = True, estado_actividad = 1).exclude(idimplemento__in=list_implementos)
    implementos2 = list(Implemento.objects.filter(estado = True, estado_actividad = 1).exclude(idimplemento__in=list_implementos))
  
    implementos3 = ImplementoSupervisor.objects.filter(estado =True, idimplemento__estado_actividad = 1).annotate(
        implemento = F('idimplemento__implemento'),
        idusuario = F('idsupervisor'),
        idusuario_id = F('idsupervisor__idusuario'),
    ).exclude(idimplementosupervisor__in=list_implementos).values('idimplemento','implemento','idusuario','idusuario_id','idimplementosupervisor')

    # Preparar los datos para la respuesta JSON
    datos_tractoristas = list(tractoristas.values('idtractorista', 'idusuario_id', 'idpersona_id__nombres', 'idpersona_id__apellidos'))  # Convierte los QuerySets a una lista de diccionarios
    datos_tractores = list(tractores2.values('idusuario', 'idusuario_id', 'idtractor', 'nrotractor', 'idfundo', 'idtractorsupervisor'))
    datos_implementos = list(implementos3.values('idimplemento', 'idusuario_id', 'implemento','idimplementosupervisor'))

    data = {
        'mensaje': "Success" if datos_tractoristas or datos_tractores else "Not found",
        'tractoristas': datos_tractoristas,
        'tractores': datos_tractores,
        'implementos': datos_implementos
    }

    return JsonResponse(data)


