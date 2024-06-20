from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from operarios.models import Tractorista
from implemento.models import Implemento
from programacion_labor.models import Programacion, DetalleLabor
from ..forms import ReporteTractorForm, ReporteTractor, Tractor
from usuario.models import Usuario
from django.http import JsonResponse

@login_required(login_url='login', redirect_field_name='')
def reportetractor(request):
    rol = request.user.idrol.rol
    if rol == "Gerencia":
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
        programacion = Programacion.objects.get(pk = programacion_id)
       
        # Creamos un reporte tractor
        reporte = ReporteTractor(idusuario = usuario, idprogramacion = programacion, horometroinicial = hora_inicial,
            horometrofinal = hora_final, correlativo = correlativo)
        reporte.save()

        # Obtenemos el id del tractorista, tractor y su hora de uso 
        tractor = Programacion.objects.filter(pk=programacion_id).values('idtractor').first()
        tractor_id = tractor['idtractor']

        horauso = Tractor.objects.filter(pk = tractor_id).values('horauso').first()
        horausoinicial = horauso['horauso']

        programa = Programacion.objects.filter(pk = programacion_id).values('idtractorista').first()
        tractorista_id = programa['idtractorista']

        # Calculando Horas de uso del tractor 
        horauso_implemento = float((hora_final - hora_inicial) *0.9)
        horauso_Detimplemento = (hora_final - hora_inicial)
        horauso_tractor = horausoinicial + (hora_final - hora_inicial)


        implementos = list(DetalleLabor.objects.filter(idprogramacion = programacion_id).values('idimplemento'))
        print(implementos)
        for implemento in implementos:
            dato = Implemento.objects.filter(idimplemento = int(implemento['idimplemento'])).values('horasdeuso').first()
            horasuso_implemento = dato['horasdeuso']

            horauso_final_implemento = horasuso_implemento + horauso_implemento

            Implemento.objects.filter(idimplemento = int(implemento['idimplemento'])).update(estado_actividad = True)
            # Implemento.objects.filter(idimplemento = int(implemento['idimplemento'])).update(horasdeuso = horauso_final_implemento)
            dato_implemento = get_object_or_404(Implemento, idimplemento = implemento['idimplemento'])
            dato_implemento.horasdeuso = horauso_final_implemento
            dato_implemento.save()
            
        # Actualizamos campos
        Programacion.objects.filter(idprogramacion = int(programacion_id)).update(estado = False)

        # DetalleLabor.objects.filter(idprogramacion = int(programacion_id)).update(estado = False)
        DetalleLabor.objects.filter(idprogramacion = int(programacion_id)).update(horadeuso = horauso_Detimplemento)
        Tractor.objects.filter(idtractor = int(tractor_id)).update(horainicial = hora_final )
        Tractor.objects.filter(idtractor = int(tractor_id)).update(horauso = horauso_tractor )
        Tractor.objects.filter(idtractor = int(tractor_id)).update(estado_actividad = True )
        Tractorista.objects.filter(idtractorista = int(tractorista_id)).update(estado_actividad = True )

       
        
        return redirect('reportetractor')
    else:
        return redirect('reportetractor')

@login_required(login_url='login', redirect_field_name='')
def obtenerHorainicial(request, id_tractor):
    tractor = list(Tractor.objects.filter(pk = id_tractor).values('horainicial'))
    if (len(tractor) >0) :
        data = {'mensaje': "Success", 'tractor': tractor}
    else:
        data = {'mensaje':"Not found"}
    return JsonResponse(data)
      
   
   
