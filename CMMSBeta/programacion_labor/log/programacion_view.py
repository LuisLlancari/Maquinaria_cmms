from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max , Count, Subquery, OuterRef
from implemento.models import *
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

#Programacion 
@login_required(login_url='login', redirect_field_name='')
def programacion(request):
    programacion = Programacion.objects.filter(estado=True)

    # Obtener subconsulta para los detalles únicos por idprogramacion
    subquery = DetalleLabor.objects.filter(
        estado=True,
        idprogramacion=OuterRef('idprogramacion')
    ).order_by('idprogramacion', 'pk')[:1]
    detalles_unicos = DetalleLabor.objects.filter(
        pk=Subquery(subquery.values('pk'))
    )

    #Obtenemos el idusuario
    usuario_id = request.user.id

    return render(request, 'programacion_labor/programacion.html', {'detalle': detalles_unicos, 'idusuario': usuario_id, 'form_programacion': ProgramacionForm, 'form_detalle': DetalleLaborForm})

def registrar_programacion(request):
    if request.method == 'POST':
        form = ProgramacionForm(request.POST)
        if form.is_valid():
            idtractor = form.cleaned_data['idtractor']
            idtractorista = form.cleaned_data['idtractorista']

            programacion = form.save()

            # Obtener el ID de la última programación guardada
            ultimo_id = Programacion.objects.aggregate(Max('idprogramacion'))['idprogramacion__max']

            # Obtener los implementos seleccionados del formulario
            implementos_seleccionados = request.POST.getlist('idimplemento')

            # Crear un detalle de labor para cada implemento seleccionado
            for implemento_id in implementos_seleccionados:
                implemento = Implemento.objects.get(pk=implemento_id)
                Implemento.objects.filter(pk = implemento_id).update(estado_actividad = False)
                DetalleLabor.objects.create(idprogramacion=programacion, idimplemento=implemento, horadeuso=0)

            Tractor.objects.filter(nrotractor = idtractor).update(estado_actividad = False)
            Tractorista.objects.filter(codigo = idtractorista).update(estado_actividad = False)

            return redirect('programacion')
    else:
        form = ProgramacionForm()
    
    return render(request, 'tu_template.html', {'form': form})

def eliminar_programacion(request, id):
    programacion = get_object_or_404(Programacion, pk=id)
    if request.method == 'POST':
        programacion.delete()
        return redirect('programacion')

def obtener_data(request, id_programacion):
    detalles_labor = DetalleLabor.objects.filter(idprogramacion=id_programacion)
    
    nombres_implementos = []
    for detalle_labor in detalles_labor:
        nombres_implementos.append(detalle_labor.idimplemento.implemento)  # Nombre del implemento

    if nombres_implementos:
        data = {'mensaje': "Success", 'nombres_implementos': nombres_implementos}
    else:
        data = {'mensaje': "Not found"}

    return JsonResponse(data)
