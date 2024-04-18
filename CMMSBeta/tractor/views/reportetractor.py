from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from programacion_labor.models import Programacion, DetalleLabor
from ..forms import ReporteTractorForm, ReporteTractor, Tractor
from usuario.models import Usuario
from django.http import JsonResponse

@login_required(login_url='login', redirect_field_name='')
def reportetractor(request):
    datos_programacion = Programacion.objects.filter(estado=True)
    print(list(datos_programacion))
    return render(request, 'tractor/reportetractor.html', {'datos': datos_programacion, 'form': ReporteTractorForm})

def registrarReporte(request):
    if request.method == 'POST':
        # Obtenemos Datos
        hora_inicial = int(request.POST.get('horometroini'))
        hora_final = int(request.POST.get('horometrofinal'))
        usuario_id  = request.POST.get('idusuario')
        programacion_id = request.POST.get('idprogramacion')
        correlativo = request.POST.get('correlativo')
       
        # Instanciamos  Clases
        usuario = Usuario.objects.get(id=usuario_id)
        programacion = Programacion.objects.get(pk = programacion_id)
       
        # Creamos un reporte tractor
        reporte = ReporteTractor(idusuario = usuario, idprogramacion = programacion, horometroinicial = hora_inicial,
            horometrofinal = hora_final, correlativo = correlativo)
        reporte.save()

        # obtenemos la hora de uso del Implemento y tractor
        tractor = Programacion.objects.filter(pk=programacion_id).values('idtractor').first()
        tractor_id = tractor['idtractor']

        horauso = Tractor.objects.filter(pk = tractor_id).values('horauso').first()
        horausoinicial = horauso['horauso']

        horauso_implemento = (hora_final - hora_inicial)
        horauso_tractor = horausoinicial + (hora_final - hora_inicial)

        # Actualizamos campos
        Programacion.objects.filter(idprogramacion = int(programacion_id)).update(estado = False)

        # DetalleLabor.objects.filter(idprogramacion = int(programacion_id)).update(estado = False)
        DetalleLabor.objects.filter(idprogramacion = int(programacion_id)).update(horadeuso = horauso_implemento)
        Tractor.objects.filter(idtractor = int(tractor_id)).update(horainicial = hora_final )
        Tractor.objects.filter(idtractor = int(tractor_id)).update(horauso = horauso_tractor )

       
        
        return redirect('reportetractor')
    else:
        return redirect('reportetractor')

def obtenerHorainicial(request, id_tractor):
    tractor = list(Tractor.objects.filter(pk = id_tractor).values('horainicial'))
    if (len(tractor) >0) :
        data = {'mensaje': "Success", 'tractor': tractor}
    else:
        data = {'mensaje':"Not found"}
    return JsonResponse(data)
      
   
   
