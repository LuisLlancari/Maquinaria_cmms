from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from mantenimiento.models import ProgramacionMantenimiento
from django.http import JsonResponse

from mantenimiento.models import Acciones, DetMotivos

# funcion que calculara las fechas de mantenimiento

def programacion_mantenimiento(request):
    datos = ProgramacionMantenimiento.objects.filter(estado= 1).annotate( )
    acciones = Acciones.objects.filter(estado__in=[0, 2])
    contexto = {
        'datos': datos,
        'acciones': acciones
    }
 
    return render(request, 'mantenimiento/programacion.html', contexto)

def registrar_fecha(request, id_implemento):
    if request.method == 'POST':
        fecha = request.POST.get('fecha_programacion')
        print(fecha)
        motivos = request.POST.getlist('idmotivo')
        print(motivos)
        id_programacion = ProgramacionMantenimiento.objects.filter(idimplemento=id_implemento).values_list('idprogramacionmantenimiento', flat=True).first()
        print(id_programacion)
        ProgramacionMantenimiento.objects.filter(idimplemento=id_implemento, estado = 1).update(fechaprogramacion=fecha)

        for idmotivo in motivos:
            DetMotivos.objects.create(idprogramacionmantenimiento_id = id_programacion, idaccion_id = idmotivo)

        
    return redirect('programacion_mantenimiento')