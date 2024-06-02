from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from mantenimiento.models import ProgramacionMantenimiento
from django.http import JsonResponse

from componente_pieza.models import DetalleComponente, DetalleConfiguracion, Componente, Pieza


from implemento.models import Implemento, TipoImplemento, DetImplementos

from mantenimiento.models import Acciones, DetMotivos

# funcion que calculara las fechas de mantenimiento

def programacion_mantenimiento(request):

    #Obtenemos el idusuario logeado
    usuario_id = request.user.id
    # print(usuario_id)

    datos = ProgramacionMantenimiento.objects.filter(estado= 1).annotate( )
    acciones = Acciones.objects.filter(estado__in=[0, 2])
    implementos = Implemento.objects.filter(estado = 1, idusuario_id = usuario_id)
    tipoimplementos = TipoImplemento.objects.filter(estado = True)
    # print(tipoimplementos)
    contexto = {
        'datos': datos,
        'acciones': acciones,
        'implementos': implementos,
        'tipoimplementos': tipoimplementos
    }
 
    return render(request, 'mantenimiento/programacion.html', contexto)

def registrar_fecha(request, id_implemento):
    if request.method == 'POST':
        fecha = request.POST.get('fecha_programacion')
        det_config = Implemento.objects.filter(idimplemento=1).annotate(
        idconfiguracion=F('idtipoimplemento__idconfiguracion_implemento__idconfiguraciontipoimplemento'),
        ).values('idconfiguracion', 'horasdeuso', 'idimplemento')

        if det_config.exists():
            # Asignamos valores del det_config a variables
            config = det_config[0]
            id_implemento = config['idimplemento']
            horauso_implemento = config['horasdeuso']
            id_configuracion = config['idconfiguracion']

            # Obtener los componentes relacionados con la configuración
            det_comp = DetalleConfiguracion.objects.filter(idconfiguracion=id_configuracion).values('idcomponente')

            for componente in det_comp:
                id_componente = componente['idcomponente']

                # Obtener las piezas relacionadas con el componente
                det_pieza = DetalleComponente.objects.filter(idcomponente=id_componente).values('iddetallecomponente','idcomponente','idpieza', 'cantidad')
                print(list(det_pieza))
                # for pieza in det_pieza:
                #     id_pieza = pieza['idpieza']
                #     cant_pieza = pieza['cantidad']

                #     # Crear instancias de los modelos relacionados
                #     inst_implemento = Implemento.objects.get(idimplemento=id_implemento)
                #     inst_componente = Componente.objects.get(idcomponente=id_componente)
                #     inst_pieza = Pieza.objects.get(idpieza=id_pieza)

                #     # Crear el detalle del implemento
                #     DetImplementos.objects.create(
                #         idimplemento=inst_implemento, 
                #         idcomponente=inst_componente,
                #         HUcomponente=horauso_implemento,
                #         idpieza=inst_pieza,
                #         HUpieza=horauso_implemento,
                #         cantidadpieza=cant_pieza)
        
    return redirect('programacion_mantenimiento')


def registrar(request):
    if request.method == 'POST':
        implemento = request.POST.get('idimplemento')
        fecha = request.POST.get('fecha_programacion')
        motivos = request.POST.getlist('idmotivo')

        # print(implemento)
        # print(fecha)
        # print(motivos)

        nueva_programacion =  ProgramacionMantenimiento.objects.create(idimplemento_id = implemento, fechaprogramacion = fecha, tipomantenimiento = 0)

        for idmotivo in motivos:
            DetMotivos.objects.create(idprogramacionmantenimiento_id = nueva_programacion.idprogramacionmantenimiento , idaccion_id = idmotivo)

    return redirect('programacion_mantenimiento')