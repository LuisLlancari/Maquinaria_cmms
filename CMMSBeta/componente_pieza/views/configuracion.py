from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import ConfiguracionTipoImplementoForms, DettaleConfiguracionForms
from django.http import JsonResponse
from django.db.models import F

#Manejo de errores
from django.contrib import messages


def configuracion(request):
  datos_configuracion = ConfiguracionTipoImplemento.objects.filter(estado=True)
  contexto = {
    'config': datos_configuracion,
    'form': ConfiguracionTipoImplementoForms,
    'comp': DettaleConfiguracionForms
  }
  return render(request, 'componente_pieza/configuracion.html', contexto)

def registrarConfiguracion(request):
  if request.method == 'POST':
    form = ConfiguracionTipoImplementoForms(request.POST)
    nom_config = request.POST.get('nombre_configuracion')
    componentes = request.POST.getlist('idcomponente')
    busqueda = ConfiguracionTipoImplemento.objects.filter(nombre_configuracion = nom_config, estado = True).exists()
    print(busqueda)
    if form.is_valid():
      if busqueda == False:
        config = form.save()
        idconfig = config.idconfiguraciontipoimplemento

        for iddetconf in componentes:
          if DetalleConfiguracion.objects.filter(idconfiguracion_id=idconfig, idcomponente_id=iddetconf).exists():
            dato = Componente.objects.get(pk=iddetconf) 
            messages.error(
                request,
                f'El componente {dato.componente} ya se encuentra registrada	.',
                extra_tags='danger'
            )
          else:
            DetalleConfiguracion.objects.create(
                idcomponente_id=iddetconf,
                idconfiguracion_id=idconfig
            )
        messages.success(request, 'Configuración registrada con éxito', extra_tags='success')
        return redirect('configuracion')
      else:
        messages.error(request, 'Ya EXISTE UNA CONFIGURACIÓN CON ESE NOMBRE', extra_tags='danger')
  else:
    messages.success(request, 'El formulario es inválido', extra_tags='danger')
  return redirect('configuracion')

def obtener (request, id_configuracion):
  componentes = list(DetalleConfiguracion.objects.filter(idconfiguracion_id=id_configuracion).annotate(
    compo = F('idcomponente__componente'),
    cod = F('idcomponente__codcomponente'),
  ). values('compo','cod'))
  if(len(componentes) > 0):
    data = {'mensaje': "Success", 'componentes': componentes}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

def eliminarConfiguracion(request, id_configuracion):
  registro = get_object_or_404(ConfiguracionTipoImplemento, pk= id_configuracion)
  if request.method == 'POST':
    idconfig = registro.idconfiguraciontipoimplemento
    det = DetalleConfiguracion.objects.filter(idconfiguracion_id=idconfig)
    print(det)
    det.estado = False
    ConfiguracionTipoImplemento.objects.filter(idconfiguraciontipoimplemento=idconfig).update(estado = False)
    messages.success(request, 'Configuración eliminada con éxito', extra_tags='success')
    return redirect('configuracion')