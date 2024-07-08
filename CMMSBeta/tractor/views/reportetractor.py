from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from operarios.models import Tractorista
from implemento.models import Implemento, ImplementoSupervisor
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.contrib import messages
from programacion_labor.models import Programacion, DetalleLabor
from ..forms import ReporteTractorForm, ReporteTractor, Tractor, TractorSupervisor
from usuario.models import Usuario
from decimal import Decimal
from django.http import JsonResponse

@login_required(login_url='login', redirect_field_name='')
def reportetractor(request):
    rol = request.user.idrol.rol
    if rol == "Asistente":
        datos_usuarios = Usuario.objects.filter(idrol = 3)
        datos_programacion = Programacion.objects.filter(estado=True)
        return render(request, 'tractor/reportetractor.html', {'datos': datos_programacion, 'form': ReporteTractorForm, 'usuarios':datos_usuarios})
    else:
        return redirect('home')
    
@login_required(login_url='login', redirect_field_name='')
def registrarReporte(request):
    if request.method == 'POST':
        # Obtenemos Datos
        hora_inicial = int(request.POST.get('horometroini'))
        hora_final = int(request.POST.get('horometrofinal'))
        usuario_id  = request.POST.get('idusuario')
        programacion_id = request.POST.get('idprogramacion')
        correlativo = request.POST.get('correlativo')
       
        # Instanciamos registros de los modelos
        usuario = Usuario.objects.get(id=usuario_id)
        programacion = Programacion.objects.get(pk=programacion_id)

        if ReporteTractor.objects.filter(correlativo=correlativo).exists():
            messages.success(request, "El CORRELATIVO YA EXISTE", extra_tags='danger')
            return redirect('reportetractor')
        else:
            # Creamos un reporte tractor
            reporte = ReporteTractor(
                idusuario=usuario, 
                idprogramacion=programacion, 
                horometroinicial=hora_inicial,
                horometrofinal=hora_final, 
                correlativo=correlativo
            )
            reporte.save()

            # Obtenemos el id del tractorista, tractor y su hora de uso 
            tractor = Programacion.objects.filter(pk=programacion_id).values('idtractor').first()
            tractor_id = tractor['idtractor']

            horauso = TractorSupervisor.objects.filter(pk=tractor_id).values('idtractor__horauso').first()
            horausoinicial = horauso['idtractor__horauso']

            programa = Programacion.objects.filter(pk=programacion_id).values('idtractorista').first()
            tractorista_id = programa['idtractorista']

            # Calculando Horas de uso del tractor 
            horauso_implemento2 = Decimal((hora_final - hora_inicial) * 0.9)
            horauso_Detimplemento = Decimal(hora_final - hora_inicial)
            horauso_tractor = Decimal(horausoinicial) + Decimal(hora_final - hora_inicial)

            implementos = list(DetalleLabor.objects.filter(idprogramacion=programacion_id).values('idimplemento'))
            for implemento in implementos:
                dato = ImplementoSupervisor.objects.filter(idimplementosupervisor=implemento['idimplemento']).values('idimplemento__horasdeuso').first()
                horasuso_implemento = Decimal(dato['idimplemento__horasdeuso'])

                horauso_final_implemento = horasuso_implemento + horauso_implemento2

                dato_implemento = get_object_or_404(ImplementoSupervisor, idimplementosupervisor=implemento['idimplemento'])
                dato_implemento.idimplemento.horasdeuso = horauso_final_implemento
                dato_implemento.idimplemento.estado_actividad = True
                dato_implemento.idimplemento.save()
                dato_implemento.save()
                
            # Actualizamos campos
            Programacion.objects.filter(idprogramacion=programacion_id).update(estado=False)
            DetalleLabor.objects.filter(idprogramacion=programacion_id).update(horadeuso=horauso_Detimplemento)

            tractor_supervisor = TractorSupervisor.objects.get(idtractorsupervisor=tractor_id)
            tractor_supervisor.idtractor.horainicial = hora_final
            tractor_supervisor.idtractor.horauso = horauso_tractor
            tractor_supervisor.idtractor.estado_actividad = True
            tractor_supervisor.idtractor.save()
            tractor_supervisor.save()

            Tractorista.objects.filter(idtractorista=tractorista_id).update(estado_actividad=True)

            return redirect('reportetractor')
    else:
        return redirect('reportetractor')

@login_required(login_url='login', redirect_field_name='')
def obtenerHorainicial(request, id_tractor):

    datos = list(Programacion.objects.filter(idprogramacion = id_tractor , estado =True).annotate(
        fundo = Concat(F('idlote__idfundo__fundo'),Value(' '),F('idlote__lote')),
        labor = F('idtipolabor__tipolabor'),
        tractor = F('idtractor__idtractor__nrotractor'),
        horainicial = F('idtractor__idtractor__horainicial'),
        fecha = F('fechahora')
    ).values('fundo','labor','tractor','fecha','horainicial'))

    # datos = list(TractorSupervisor.objects.filter(idtractor = 11).values())
    # print(datos)

    if (len(datos) >0) :
        data = {'mensaje': "Success", 'tractor': datos}
    else:
        data = {'mensaje':"Not found"}
    return JsonResponse(data)
      
   
   
