from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import DettaleConfiguracionForms
from django.http import JsonResponse

#Manejo de errores
from django.contrib import messages


def detalle_cong(request):
    lista_cong = DetalleConfiguracion.objects.filter(estado=True).order_by('idconfiguracion')
    contexto = {
        'lista_cong': lista_cong,
        'form': DettaleConfiguracionForms
    }
    return render(request, 'componente_pieza/detalle_cong.html', contexto)



def registrarDetalleConfiguracion(request):
    if request.method == 'POST':
        idconfig = request.POST.get('idconfiguracion')
        componentes = request.POST.getlist('idcomponente')

        print(idconfig)
        print(componentes)

        for idcomponente in componentes:
            if DetalleConfiguracion.objects.filter(idconfiguracion_id=idconfig, idcomponente_id=idcomponente).exists():
                dato = Componente.objects.get(pk=idcomponente) 
                messages.error(
                    request,
                    f'El componente {dato.componente} ya se encuentra registrada	.',
                    extra_tags='danger'
                )           
            else:
                DetalleConfiguracion.objects.create(
                    idcomponente_id=idcomponente,
                    idconfiguracion_id=idconfig,
                )

        return redirect('detalle_cong')

    return redirect('detalle_cong')