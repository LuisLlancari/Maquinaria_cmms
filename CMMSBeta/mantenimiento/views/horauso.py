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

    implementos = Implemento.objects.select_related(
        'idtipoimplemento__idconfiguracion_implemento'
    ).prefetch_related(
        Prefetch(
            'idtipoimplemento__idconfiguracion_implemento__dettaleconfiguracion_set',
            queryset=DettaleConfiguracion.objects.select_related('idcomponente')
        ),
        Prefetch(
            'idtipoimplemento__idconfiguracion_implemento__dettaleconfiguracion_set__idcomponente__pieza_set'
        )
    )

    data = []

    for implemento in implementos:
        hora_de_uso = implemento.horasdeuso
        frecuencia_mantenimiento = implemento.idtipoimplemento.frecuencia_man
        
        # Verificar que frecuencia_mantenimiento y hora_de_uso no sean None
        if frecuencia_mantenimiento is not None and hora_de_uso is not None:
            proximo_mantenimiento, mantenimiento_realizados = calculo_horas(frecuencia_mantenimiento, hora_de_uso)
            
            implemento_data = {
                'implemento': implemento.implemento,
                'mantenimiento_realizados': mantenimiento_realizados,
                'proximo_mantenimiento': proximo_mantenimiento,
                'configuracion': implemento.idtipoimplemento.idconfiguracion_implemento.nombre_configuracion,
                'detalles': []
            }
            
            configuracion = implemento.idtipoimplemento.idconfiguracion_implemento
            detalles = configuracion.dettaleconfiguracion_set.all()

            for detalle in detalles:
                componente = detalle.idcomponente
                frecuencia_mantenimiento = componente.frecuencia_man

                # Verificar que frecuencia_mantenimiento y hora_de_uso no sean None
                if frecuencia_mantenimiento is not None:
                    proximo_mantenimiento, mantenimiento_realizados = calculo_horas(frecuencia_mantenimiento, hora_de_uso)
                    
                    detalle_data = {
                        'componente': componente.componente,
                        'frecuencia_mantenimiento': frecuencia_mantenimiento,
                        'mantenimiento_realizados': mantenimiento_realizados,
                        'proximo_mantenimiento': proximo_mantenimiento,
                        'piezas': []
                    }
                    
                    piezas = componente.pieza_set.all()
                    for pieza in piezas:
                        frecuencia_mantenimiento = pieza.frecuencia_man

                        # Verificar que frecuencia_mantenimiento y hora_de_uso no sean None
                        if frecuencia_mantenimiento is not None:
                            proximo_mantenimiento, mantenimiento_realizados = calculo_horas(frecuencia_mantenimiento, hora_de_uso)
                            
                            pieza_data = {
                                'pieza': pieza.pieza,
                                'frecuencia_mantenimiento': frecuencia_mantenimiento,
                                'mantenimiento_realizados': mantenimiento_realizados,
                                'proximo_mantenimiento': proximo_mantenimiento
                            }
                            
                            detalle_data['piezas'].append(pieza_data)
                    
                    implemento_data['detalles'].append(detalle_data)
            
            data.append(implemento_data)
    
    context = {
        'data': data
    }
  
    return JsonResponse(context)
    # return render(request, 'mantenimiento/horasdeuso.html' )