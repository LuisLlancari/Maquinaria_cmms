from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Tractor, TipoTractor, TractorSupervisor
from ..forms import TractorForm
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Value, F, CharField, IntegerField
from django.db.models.functions import Concat, Coalesce
from django.utils import timezone
from fundo_cultivo.models import Fundo
from usuario.models import Usuario


@login_required(login_url='login', redirect_field_name='')
def tractor(request):

    rol_usuario = request.user.idrol.rol
    id_usuario = request.user.id
    if rol_usuario == "Supervisor":
        tractores = TractorSupervisor.objects.filter(estado = True , idsupervisor = id_usuario).annotate(
            idtipotractor = F('idtractor__idtipotractor__TipoTractor'),
            idusuario =F('idsupervisor__first_name'),
            idfundo =F('idtractor__idfundo__fundo'),
            nrotractor =F('idtractor__nrotractor'),
            horainicial =F('idtractor__horainicial'),
            horauso =F('idtractor__horauso'),
        ).values('idtractor', 'idtipotractor','idusuario','idfundo','nrotractor','horainicial','horauso')

        tipotractor = TipoTractor.objects.filter(estado = True)
        fundo = Fundo.objects.filter(estado = True)
        usuario = Usuario.objects.filter(idrol = 3) 
        form = TractorForm()
        data = {
            'tractores' : tractores,
            'form' : form,
            'tipotractor' : tipotractor,
            'fundo' : fundo,
            'usuario' : usuario
        }
        
        return render(request, 'tractor/tractor.html', data)
    
    elif rol_usuario == "Admin":

        tractores_queryset = Tractor.objects.filter(estado = True).annotate(
        idusuario=Coalesce(
            Subquery(
                TractorSupervisor.objects.filter(
                    idtractor_id=OuterRef('pk'),
                    estado = True
                ).values('idsupervisor_id')[:1]
            ),
            Value(None),
            output_field=IntegerField()
        ),
        supervisor_nombre=Coalesce(
            Subquery(
                TractorSupervisor.objects.filter(
                    idtractor_id=OuterRef('pk'),
                    estado = True
                ).values('idsupervisor__first_name')[:1]
            ),
            Value('No definido'),
            output_field=CharField()
        ),
        supervisor_apellido=Coalesce(
            Subquery(
                TractorSupervisor.objects.filter(
                    idtractor_id=OuterRef('pk'),
                    estado = True
                ).values('idsupervisor__last_name')[:1]
            ),
            Value(''),
            output_field=CharField()
        )
        ).annotate(
            supervisor_nombre_completo=Concat(
                'supervisor_nombre',
                Value(' '),
                'supervisor_apellido'
            )
        )

        # tractores = Tractor.objects.filter(estado = True)
        tipotractor = TipoTractor.objects.filter(estado = True)
        fundo = Fundo.objects.filter(estado = True)
        usuario = Usuario.objects.filter(idrol = 3) 
        form = TractorForm()
        data = {
            'tractores' : tractores_queryset,
            'form' : form,
            'tipotractor' : tipotractor,
            'fundo' : fundo,
            'usuario' : usuario
        }
        
        return render(request, 'tractor/tractor.html', data)
    else:
        return redirect('home')

@login_required(login_url='login', redirect_field_name='')
def eliminar_tractor(request, idtractor):
    tractor = get_object_or_404(Tractor, pk = idtractor)
    if request.method == 'POST':
        tractor.estado = False
        tractor.save()
        return redirect('tractor')
    
@login_required(login_url='login', redirect_field_name='')
def registrar_tractor(request):
    if request.method == 'POST':
        form = TractorForm(request.POST)
        nom_tractor = request.POST.get('nrotractor').strip()
        existe_tractor = Tractor.objects.filter(nrotractor = nom_tractor, estado = True).exists()
        if form.is_valid() and existe_tractor == False:
            form.save()
            messages.success(request, "El tractor ha sido agregado correctamente", extra_tags='success')
            return redirect('tractor')
        else:
            messages.success(request, "El tractor ya existe", extra_tags='warning')
            return redirect('tractor')
    else:
        return redirect('tractor')
    
@login_required(login_url='login', redirect_field_name='')
def editar_tractor(request):
    if request.method == 'POST':
        idtractor = request.POST.get('idtractor')

        nom_tractor = request.POST.get('nrotractor').strip()
        idusuario = request.POST.get('idusuario')
        idfundo = request.POST.get('idfundo')

        print(nom_tractor)
        print(idusuario)
        print(idfundo)
        tractor = get_object_or_404(Tractor, pk = idtractor)
        form = TractorForm(request.POST, instance=tractor)

        existe_tractor = Tractor.objects.filter(nrotractor = nom_tractor, idusuario = idusuario, idfundo = idfundo, estado = True).exists()
        print(existe_tractor)
        if form.is_valid() and existe_tractor == False:
            form.save()
            messages.success(request, "El tractor ha sido modificado correctamente", extra_tags='primary')
            return redirect('tractor')
        else:
            # errores = form.errors.as_text()
            # mensaje_error = f"Hubo un error: {errores}"
            # return HttpResponse(mensaje_error)
            messages.success(request, "El tractor ya existe ", extra_tags='warning')
            return redirect('tractor')
    else:
        return redirect('tractor')

@login_required(login_url='login', redirect_field_name='')
def AsignarSupervisor(request, id_tractor):
  if request.method == "POST":

    ahora = timezone.localtime()
    fecha_actual = ahora.date()
    usuario = request.POST.get('select-usuario')
    TractorSupervisor.objects.create(idsupervisor_id=usuario, idtractor_id=id_tractor, fechaInicio=fecha_actual)

    messages.success(request, 'Supervisor asignado con éxito', extra_tags='success')
    return redirect('tractor')

@login_required(login_url='login', redirect_field_name='')
def QuitarSupervisor(request, id_tractor):
  if request.method == "POST":

    usuario = request.POST.get('select-usuario')
    ahora = timezone.localtime()
    fecha_actual = ahora.date()

    tratorsup = get_object_or_404(TractorSupervisor, idtractor = id_tractor, estado=True)
    tratorsup.fechaFin = fecha_actual
    tratorsup.estado = False
    tratorsup.save()

    TractorSupervisor.objects.create(idsupervisor_id=usuario, idtractor_id=id_tractor, fechaInicio=fecha_actual)

    messages.success(request, 'Supervisor modificado con éxito', extra_tags='success')
    return redirect('tractor')



    

    


