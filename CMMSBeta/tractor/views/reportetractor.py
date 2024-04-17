from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from programacion_labor.models import Programacion, DetalleLabor
from ..forms import ReporteTractorForm, ReporteTractor, Tractor
from usuario.models import Usuario

@login_required(login_url='login', redirect_field_name='')
def reportetractor(request):
    datos_programacion = Programacion.objects.filter(estado=True)
    print(list(datos_programacion))
    return render(request, 'tractor/reportetractor.html', {'datos': datos_programacion, 'form': ReporteTractorForm})

def registrarReporte(request):
    if request.method == 'POST':
        # Obtenemos Datos
        hora_inicial = int(request.POST.get('horometroinicial'))
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
        horauso_detalle= (hora_final - hora_inicial)

        # Actualizamos campos
        Programacion.objects.filter(idprogramacion = int(programacion_id)).update(estado = False)
        print(f"esta es la{horauso_detalle}")
        DetalleLabor.objects.filter(idprogramacion = int(programacion_id)).update(estado = False)
        DetalleLabor.objects.filter(idprogramacion = int(programacion_id)).update(horadeuso = horauso_detalle)
        Tractor.objects.filter(idtractor = int(tractor_id)).update(horauso = horauso_detalle )

       
        
        return redirect('reportetractor')
    else:
        return redirect('reportetractor')

    

   
   
