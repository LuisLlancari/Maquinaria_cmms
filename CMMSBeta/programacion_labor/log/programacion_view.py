from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max
from implemento.models import *

from django.contrib.auth.decorators import login_required

#Programacion 
@login_required(login_url='login', redirect_field_name='')
def programacion(request):
    programacion = Programacion.objects.filter(estado=True)

    # Diccionario de mapeo de letras a palabras
    turno_map = {'M': 'Manaña', 'T': 'Tarde', 'N': 'Noche'}

    # Mapeo de los turnos
    for prog in programacion:
        prog.turno = turno_map.get(prog.turno, 'Desconocido')

    return render(request, 'programacion_labor/programacion.html', {'datos': programacion, 'form_programacion': ProgramacionForm , 'form_detalle': DetalleLaborForm})


def registrar_programacion(request):
    if request.method == 'POST':
        form = ProgramacionForm(request.POST)
        if form.is_valid():
            programacion = form.save()

            # Obtener el ID de la última programación guardada
            ultimo_id = Programacion.objects.aggregate(Max('idprogramacion'))['idprogramacion__max']

            # Obtener los implementos seleccionados del formulario
            implementos_seleccionados = request.POST.getlist('idimplemento')

            # Crear un detalle de labor para cada implemento seleccionado
            for implemento_id in implementos_seleccionados:
                implemento = Implemento.objects.get(pk=implemento_id)
                DetalleLabor.objects.create(idprogramacion=programacion, idimplemento=implemento, horadeuso='08:00:00')

            return redirect('programacion')
    else:
        form = ProgramacionForm()
    
    return render(request, 'tu_template.html', {'form': form})