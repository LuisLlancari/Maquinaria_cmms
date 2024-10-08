from django.shortcuts import render, redirect, get_object_or_404
from ..models import Componente
from ..forms import ComponenteForms, DetalleComponenteForms
from django.http import JsonResponse
from ..models import DetalleComponente, Pieza
from django.db.models import F

#Manejo de errores
from django.contrib import messages

def componente(request):
  datos_componente = Componente.objects.filter(estado =True)
  return render(request, 'componente_pieza/componente.html',{'datos_componente':datos_componente, 'form':ComponenteForms, 'det':DetalleComponenteForms})

def registrarComponente(request):
  if request.method == 'POST':
      form = ComponenteForms(request.POST)
      cod_compo = request.POST.get('codcomponente')
      piezas = request.POST.getlist('idpieza')
      cantidades = request.POST.getlist('cantidad')
      busqueda = Componente.objects.filter(codcomponente = cod_compo, estado = True).exists()
      print(busqueda)
      if form.is_valid():  # Verifica si los datos son válidos
        if busqueda == False:
          componente = form.save()
          idcomponente = componente.idcomponente

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

            messages.success(request, 'Componente registrado con exito', extra_tags='success')
            return redirect('componente')
        else:
          messages.error(request, 'El componente ya existe', extra_tags='danger')
          return redirect('componente')
  else:
      messages.error(request, 'El formulario es inválido', extra_tags='danger')
  
  return redirect('componente')

def eliminarComponente(request, id_componente):
  registro = get_object_or_404(Componente, pk= id_componente)
  if request.method == 'POST':
    idcomponente = registro.idcomponente
    det = DetalleComponente.objects.filter(idcomponente_id=idcomponente)
    print(det)
    det.estado = False
    Componente.objects.filter(idcomponente=idcomponente).update(estado = False)
    messages.success(request, 'Componente eliminado con exito', extra_tags='success')

    return redirect('componente')
  
def editarComponente(request, id_componente):
  sistema = get_object_or_404(Componente, pk=id_componente)
  form = ComponenteForms(request.POST, instance=sistema)
  form.save()
  return redirect('componente')

def obtenerDatos(request, id_componente):
  componentes = list(Componente.objects.filter(pk=id_componente).values())
  print(componentes)
  if(len(componentes) > 0):
    data = {'mensaje': "Success", 'componentes': componentes}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)

def obtenerPiezas(request, id_componente):
  #PARA OBTENER MAS ESPECIFICA LA CONSULTA
  piezas = list(DetalleComponente.objects.filter(idcomponente_id=id_componente).annotate(
    pieza = F('idpieza__pieza'),
  ). values('pieza','cantidad'))
  if(len(piezas) > 0):
    data = {'mensaje': "Success", 'piezas': piezas}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)