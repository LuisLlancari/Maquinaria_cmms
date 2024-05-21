from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from implemento.models import Implemento
from componente_pieza.models import DettaleConfiguracion
from django.db.models import F
from django.db.models import Prefetch
from django.http import JsonResponse

# funcion que calculara las fechas de mantenimiento

def calculo_horas(FM, HU):
    if FM is None or HU is None:
        return 0, 0
    if HU < FM:
        proximo_M = FM - HU
        mantenimientos_realizados = 0
    else:
        mantenimientos_realizados = HU // FM
        proximo_M = FM - (HU % FM)
    return proximo_M, mantenimientos_realizados


def horasuso(request):
    
    det_config = (
        Implemento.objects.annotate(
            configuracion=F('idtipoimplemento__idconfiguracion_implemento__nombre_configuracion')
        ).values('configuracion').first()
    )
    algo = det_config[0]
   
    data = {'hora': algo['configuracion'], 'configuracion' : det_config}
    return JsonResponse(data)