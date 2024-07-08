from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Implemento, ImplementoSupervisor
from ..forms import ImplementoForms
from usuario.models import Usuario
from django.http import JsonResponse
from django.db.models import OuterRef, Subquery, Value, F, CharField, IntegerField
from django.utils import timezone
from django.db.models.functions import Concat, Coalesce



#Manejo de errores
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='implemento')
def implemento(request):
  # Obtenemos el Rol y ID del usuario 
  rol_usuario = request.user.idrol.rol
  id_usuario = request.user.id

  # Comparamos el Rol 
  if rol_usuario == "Supervisor":

    datos_implemento = ImplementoSupervisor.objects.filter(estado=True, idsupervisor=id_usuario).annotate(
      idusuario=F('idsupervisor'),
      implemento = F('idimplemento__implemento'),
      idtipoimplemento =F('idimplemento__idtipoimplemento__tipoimplemento'),
      tiempo_vida =F('idimplemento__idtipoimplemento__tiempo_vida'),
      frecuencia_man =F('idimplemento__idtipoimplemento__frecuencia_man'),
      codimplemento =F('idimplemento__codimplemento'),
      idceco =F('idimplemento__idceco__ceco'),
      horasdeuso =F('idimplemento__horasdeuso'),
    ).values('idusuario', 'idtipoimplemento', 'tiempo_vida', 'frecuencia_man', 'codimplemento', 'idceco','implemento','horasdeuso')

    usuarios = Usuario.objects.filter(is_active = True, idrol__rol = "Supervisor")
    return render(request, 'implemento/implemento.html', {'datos': datos_implemento, 'form':ImplementoForms, 'usuarios':usuarios})
  
  elif rol_usuario == "Admin":
    
    implementos_consulta = Implemento.objects.filter(estado =True).annotate(
    idusuario=Coalesce(
        Subquery(
            ImplementoSupervisor.objects.filter(
                idimplemento_id=OuterRef('pk'),
                estado=True
            ).values('idsupervisor_id')[:1]
        ),
        Value(None),
        output_field=IntegerField()
    ),
    supervisor_nombre=Coalesce(
        Subquery(
            ImplementoSupervisor.objects.filter(
                idimplemento_id=OuterRef('pk'),
                estado=True
            ).values('idsupervisor__first_name')[:1]
        ),
        Value('No definido'),
        output_field=CharField()
    ),
    supervisor_apellido=Coalesce(
        Subquery(
            ImplementoSupervisor.objects.filter(
                idimplemento_id=OuterRef('pk'), 
                estado=True
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

    usuarios = Usuario.objects.filter(is_active = True, idrol__rol = "Supervisor")
    datos_implemento = Implemento.objects.filter(estado = True) 
    return render(request, 'implemento/implemento.html', {'datos': implementos_consulta, 'form':ImplementoForms, 'usuarios':usuarios})
  else:
    return redirect('home')

@login_required(login_url='login', redirect_field_name='')
def registrarImplemento(request):
  if request.method == 'POST':
    nom_implemento = request.POST.get('implemento').strip()
    cod_implemento = request.POST.get('codimplemento').strip()
    existe_nom = Implemento.objects.filter(implemento = nom_implemento, estado = True).exists()
    existe_cod = Implemento.objects.filter(codimplemento = cod_implemento, estado = True).exists()
    form = ImplementoForms(request.POST)
    if form.is_valid() and existe_nom == False and existe_cod == False:
      form.save()
      messages.success(request, 'Implemento registrado con exito', extra_tags='success')
      return redirect('implemento')
    else:
      messages.error(request, 'El implemento ya existe', extra_tags='danger')

  return redirect('implemento')

@login_required(login_url='login', redirect_field_name='')
def eliminarimplemento(request, id_implemento):
  registro = get_object_or_404(Implemento, pk= id_implemento)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('implemento')
  
@login_required(login_url='login', redirect_field_name='')
def editarImplemento(request, id_implemento):
  if request.method == 'POST':
    implemento = get_object_or_404(Implemento, pk=id_implemento)
    form = ImplementoForms(request.POST, instance=implemento)
    nom_implemento = request.POST.get('implemento').strip()
    cod_implemento = request.POST.get('codimplemento').strip()
    existe_nom = Implemento.objects.filter(implemento = nom_implemento, estado = True).exists()
    existe_cod = Implemento.objects.filter(codimplemento = cod_implemento, estado = True).exists()
    if form.is_valid() and existe_nom == False or existe_cod == False:
      form.save()
      messages.success(request, 'Implemento editado con exito', extra_tags='primary')
      return redirect('implemento')
    else:
      messages.error(request, 'El implemento ya existe', extra_tags='danger')
      return redirect('implemento')
  return redirect('implemento')

@login_required(login_url='login', redirect_field_name='')
def obtenerDatos(request, id_implemento):
  implemento = list(Implemento.objects.filter(pk=id_implemento).values())
  if(len(implemento) > 0):
    data = {'mensaje': "Success", 'implemento': implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

@login_required(login_url='login', redirect_field_name='')
def AsignarSupervisor(request, id_implemento):
  if request.method == "POST":

    ahora = timezone.localtime()
    fecha_actual = ahora.date()
    usuario = request.POST.get('select-usuario')
    ImplementoSupervisor.objects.create(idsupervisor_id=usuario, idimplemento_id=id_implemento, fechaInicio=fecha_actual)

    messages.success(request, 'Supervisor asignado con éxito', extra_tags='success')
    return redirect('implemento')


  
@login_required(login_url='login', redirect_field_name='')
def QuitarSupervisor(request, id_implemento):
  if request.method == "POST":

    usuario = request.POST.get('select-usuario')
    ahora = timezone.localtime()
    fecha_actual = ahora.date()

    implementosup = get_object_or_404(ImplementoSupervisor, idimplemento = id_implemento, estado=True)
    implementosup.fechaFin = fecha_actual
    implementosup.estado = False
    implementosup.save()

    ImplementoSupervisor.objects.create(idsupervisor_id=usuario, idimplemento_id=id_implemento, fechaInicio=fecha_actual)

    messages.success(request, 'Supervisor modificado con éxito', extra_tags='success')
    return redirect('implemento')
