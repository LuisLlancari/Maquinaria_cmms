from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from mantenimiento.models import ProgramacionMantenimiento
from django.http import JsonResponse

# funcion que calculara las fechas de mantenimiento

def programacion_mantenimiento(request):
    datos =(
        ProgramacionMantenimiento.objects.filter(estado= 1).annotate( )
    )
 
    return render(request, 'mantenimiento/programacion.html', {'datos':datos})

def registrar_fecha(request, id_implemento):
    if request.method == 'POST':
        fecha = request.POST.get('fecha_programacion')
        ProgramacionMantenimiento.objects.filter(idimplemento=id_implemento, estado = 1).update(fechaprogramacion=fecha)
        
    return redirect('programacion_mantenimiento')