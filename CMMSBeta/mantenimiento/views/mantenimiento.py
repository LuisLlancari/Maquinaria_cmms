from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from ..models import Mantenimiento, ProgramacionMatenimiento

from django.contrib.auth.decorators import login_required
def mantenimiento(request):
    datos = Mantenimiento.objects.filter(estado = True)
    return render(request, 'mantenimiento/mantenimiento.html', {'datos': datos})

def registrar_mantenimiento(request):
    if request.method == 'POST':
        pass
    else:
        return redirect('mantenimiento')
    
def modificar_mantenimiento(request, id_mantenimiento):
    if request.method == 'POST':
        pass
    else:
        return redirect('mantenimiento')
    
def crear_diagnostico(request):
    mantenimiento = list(Mantenimiento.objects.filter(estado=True).values())
    if(len(mantenimiento) > 0):
        data = {'mensaje': "Success", 'mantenimiento': mantenimiento}
    else:
        data = {'mensaje':"Not found"}
    return JsonResponse(data)