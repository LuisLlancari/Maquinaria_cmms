from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from mantenimiento.models import ProgramacionMantenimiento
from django.http import JsonResponse

from implemento.models import Implemento, TipoImplemento

from mantenimiento.models import Acciones, DetMotivos

# funcion que calculara las fechas de mantenimiento

def programacion_mantenimiento(request):

    #Obtenemos el idusuario logeado
    usuario_id = request.user.id
    print(usuario_id)

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
        # print(fecha)
        motivos = request.POST.getlist('idmotivo')
        # print(motivos)
        # id_programacion = ProgramacionMantenimiento.objects.filter(idimplemento=id_implemento).values_list('idprogramacionmantenimiento', flat=True).first()
        # print(id_programacion)

        #ProgramacionMantenimiento.objects.filter(idprogramacionmantenimiento=id_implemento, estado = 1).update(fechaprogramacion=fecha)
       
       # Actaulizar Programacion con un save

        programacion = get_object_or_404(ProgramacionMantenimiento, idprogramacionmantenimiento=id_implemento, estado=1)
        programacion.fechaprogramacion = fecha
        programacion.save()

        for idmotivo in motivos:
            DetMotivos.objects.create(idprogramacionmantenimiento_id = id_implemento, idaccion_id = idmotivo)

        
    return redirect('programacion_mantenimiento')


def registrar(request):
    if request.method == 'POST':
        implemento = request.POST.get('idimplemento')
        fecha = request.POST.get('fecha_programacion')
        motivos = request.POST.getlist('idmotivo')

        print(implemento)
        print(fecha)
        print(motivos)

        nueva_programacion =  ProgramacionMantenimiento.objects.create(idimplemento_id = implemento, fechaprogramacion = fecha, tipomantenimiento = 0)

        for idmotivo in motivos:
            DetMotivos.objects.create(idprogramacionmantenimiento_id = nueva_programacion.idprogramacionmantenimiento , idaccion_id = idmotivo)

    return redirect('programacion_mantenimiento')