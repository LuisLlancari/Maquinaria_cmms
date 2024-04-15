from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

#Programacion 
@login_required(login_url='login', redirect_field_name='')
def programacion(request):
    programacion = Programacion.objects.filter(estado=True)
    for programacion in programacion:
        programacion.turno = 'M' if programacion.turno == 'M' else 'T' if programacion.turno == 'T' else 'N'

    return render(request, 'programacion_labor/programacion.html', {'datos': programacion, 'form_programacion': ProgramacionForm })