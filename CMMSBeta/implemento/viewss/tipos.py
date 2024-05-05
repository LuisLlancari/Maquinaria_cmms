from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import TipoImplemento
from ..forms import TipoImplementoForms
from django.http import JsonResponse


#Manejo de errores
from django.contrib import messages

def tipoImplemento (request):
  datos_tipoimplemento = TipoImplemento.objects.filter(estado=True)
  return render(request, 'implemento/tipoimplemento.html', {'datos': datos_tipoimplemento, 'form': TipoImplementoForms})


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

def eliminarImplemento(request, id):
  registro = get_object_or_404(TipoImplemento, pk= id)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('tipoimplemento')
  
def editarTipoImplemento(request, id_tipo):
  if request.method == 'POST':
    tipo_implmento = get_object_or_404(TipoImplemento, pk=id_tipo)
    form = TipoImplementoForms(request.POST, instance=tipo_implmento)
    tipoimplemento = request.POST.get('tipoimplemento')
    #Verificamos si el tipo de implemento ya existe
    existe_implemento = TipoImplemento.objects.filter(tipoimplemento=tipoimplemento, estado=True).exists()
    print(existe_implemento)
    if form.is_valid():
      if existe_implemento == False:
        messages.success(request, 'Tipo de implemento actualizado con éxito', extra_tags='success')
        form.save()
      else:
        messages.error(request, 'El tipo de implemento ya existe', extra_tags='danger')
  return redirect('tipoimplemento')


def obtenerDatos(request, id_tipo):
  tipo_implemento = list(TipoImplemento.objects.filter(pk=id_tipo).values())
  if(len(tipo_implemento) > 0):
    data = {'mensaje': "Success", 'tipos': tipo_implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

