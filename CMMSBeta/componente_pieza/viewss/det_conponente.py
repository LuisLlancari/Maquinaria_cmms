from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import DetalleComponenteForms
from django.http import JsonResponse

#Manejo de errores
from django.contrib import messages

def det_componente(request):
  lista_componente = DetalleComponente.objects.filter(estado=True)
  contexto = {
    'lista_componente': lista_componente,
    'form': DetalleComponenteForms
    
  }
  return render(request, 'componente_pieza/det_componente.html', contexto)

def registrarDetalleComponente(request):
    if request.method == 'POST':
        idcomponente = request.POST.get('idcomponente')
        piezas = request.POST.getlist('idpieza')
        cantidades = request.POST.getlist('cantidad')

        for idpieza, cantidad in zip(piezas, cantidades):
            if DetalleComponente.objects.filter(idcomponente_id=idcomponente, idpieza_id=idpieza).exists():
                dato = Pieza.objects.get(pk=idpieza) 
                messages.error(
                    request,
                    f'La pieza {dato.pieza} ya se encuentra registrada	.',
                    extra_tags='danger'
                )           
            else:
                DetalleComponente.objects.create(
                    idcomponente_id=idcomponente,
                    idpieza_id=idpieza,
                    cantidad=cantidad
                )

        return redirect('det_componente')

    return redirect('det_componente')