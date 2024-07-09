from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import TipoImplemento
from ..forms import TipoImplementoForms
from django.http import JsonResponse
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='')
def tipoImplemento (request):
  rol = request.user.idrol.rol
  if rol == "Admin":
    datos_tipoimplemento = TipoImplemento.objects.filter(estado=True)
    return render(request, 'implemento/tipoimplemento.html', {'datos': datos_tipoimplemento, 'form': TipoImplementoForms})
  else:
    return redirect('home')
  
@login_required(login_url='login', redirect_field_name='')
def registrarTipoImplemento(request):
    if request.method == 'POST':
        form = TipoImplementoForms(request.POST)
        tipoimplemento = request.POST.get('tipoimplemento')
        #Verificamos si el tipo de implemento ya existe
        existe_implemento = TipoImplemento.objects.filter(tipoimplemento=tipoimplemento, estado=True).exists()
        print(existe_implemento)
        if form.is_valid():
            if existe_implemento == False:
                messages.success(request, 'Tipo de implemento registrado con éxito', extra_tags='success')
                form.save()
            else:
                messages.error(request, 'El tipo de implemento ya existe', extra_tags='danger')
        else:
            messages.error(request, 'El formulario es inválido', extra_tags='danger')
    return redirect('tipoimplemento')

@login_required(login_url='login', redirect_field_name='')
def eliminarImplemento(request, id):
  registro = get_object_or_404(TipoImplemento, pk= id)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tipoimplemento')

@login_required(login_url='login', redirect_field_name='')  
def editarTipoImplemento(request, id_tipo):
  if request.method == 'POST':
    tipo_implmento = get_object_or_404(TipoImplemento, pk=id_tipo)
    tiempo_vida = request.POST.get('tiempo_vida')
    print(tiempo_vida)
    frecuencia_man = request.POST.get('frecuencia_man')
    print(frecuencia_man)
    form = TipoImplementoForms(request.POST, instance=tipo_implmento)
    tipoimplemento = request.POST.get('tipoimplemento')
    #Verificamos si el tipo de implemento ya existe
    existe_implemento = TipoImplemento.objects.filter(tipoimplemento=tipoimplemento, tiempo_vida=tiempo_vida, frecuencia_man=frecuencia_man, estado=True).exists()
    print(existe_implemento)
    if form.is_valid():
      if existe_implemento == False:
        messages.success(request, 'Tipo de implemento actualizado con éxito', extra_tags='success')
        form.save()
      else:
        messages.error(request, 'El tipo de implemento ya existe', extra_tags='danger')
  return redirect('tipoimplemento')

@login_required(login_url='login', redirect_field_name='')
def obtenerDatos(request, id_tipo):
  tipo_implemento = list(TipoImplemento.objects.filter(pk=id_tipo).values())
  if(len(tipo_implemento) > 0):
    data = {'mensaje': "Success", 'tipos': tipo_implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

