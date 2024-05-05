from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max , Count, Subquery, OuterRef
from implemento.models import *
from django.http import JsonResponse
from django.contrib import messages

from django.utils import timezone

from implemento.models import *

from usuario.models import *

from operarios.models import *
from tractor.models import *
from fundo_cultivo.models import *

from django.contrib.auth.decorators import login_required

#Programacion 
@login_required(login_url='login', redirect_field_name='')
def programacion(request):
    programacion = Programacion.objects.filter(estado=True)

    # Obtener la cantidad de tractores utilizados hoy
    hoy = timezone.now().date()
    print(hoy)
    cantidad_tractores_hoy = Programacion.objects.filter(fechahora=hoy, idusuario = request.user).count()
    print(cantidad_tractores_hoy)


    #Obtenemos el idusuario
    usuario_id = request.user.id
    tractoristas = Tractorista.objects.filter(estado = True, estado_actividad = True)
    tractor = Tractor.objects.filter(estado = True, estado_actividad = True)
    fundos = Fundo.objects.filter(estado = True)
    lotes = Lote.objects.filter(estado = True)
    detalles = DetalleLabor.objects.filter(estado = True, idprogramacion__idusuario = usuario_id)

    #Obtenemos detalles unicos
    subquery = DetalleLabor.objects.filter(
    estado=True,
    idprogramacion=OuterRef('idprogramacion'),
    idprogramacion__idusuario=usuario_id
    ).order_by('idprogramacion__fechahora')[:1]

    # Obtener los detalles únicos por idprogramacion y ordenarlos de forma ascendente por la fecha de idprogramacion
    detalles_unicos = DetalleLabor.objects.filter(
        pk=Subquery(subquery.values('pk'))
    ).order_by('-idprogramacion__fechahora')


    #LISTA DE USUARIO PARA EL SELECT 
    usuario = Usuario.objects.filter(idrol = 3)

    implementos = Implemento.objects.filter(estado_actividad = True, estado = True)

    return render(request, 'programacion_labor/programacion.html', {'cantidad': cantidad_tractores_hoy , 'fecha': hoy, 'detalle': detalles_unicos, 'tractor' : tractor , 'tractorista': tractoristas ,'idusuario': usuario_id, 'lista_usuarios': usuario ,'fundo': fundos,'lotes': lotes,'form_programacion': ProgramacionForm, 'implementos': implementos})

def registrar_programacion(request):
    if request.method == 'POST':
        form = ProgramacionForm(request.POST)
        if form.is_valid():
            idtractor = form.cleaned_data['idtractor']
            # idtractorista = form.cleaned_data['idtractorista']
            idtractorista = request.POST.get('idtractorista')

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
            Tractorista.objects.filter(pk = idtractorista).update(estado_actividad = False)

            messages.success(request, "La programacion ha sido agregada correctamente", extra_tags='success')
            return redirect('programacion')
    else:
        messages.success(request, "Ingrese datos válidos", extra_tags='danger')
        return redirect('programacion')

def eliminar_programacion(request, id_programacion):
    programacion = get_object_or_404(DetalleLabor, pk=id_programacion)
    if request.method == 'POST':
        programacion.estado = False
        programacion.save()
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
