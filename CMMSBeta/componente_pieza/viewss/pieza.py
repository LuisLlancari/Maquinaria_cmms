from django.shortcuts import render, redirect, get_object_or_404
from ..models import Pieza
from ..forms import PiezaForms
from django.http import JsonResponse

# Vista de Piezas
def pieza(request):
  datos_pieza = Pieza.objects.filter(estado=True)
  return render(request, 'componente_pieza/pieza.html',{'datos_pieza':datos_pieza, 'form':PiezaForms})

def registrarPieza(request):
  if request.method == 'POST':
    form = PiezaForms(request.POST)
    if form.is_valid():
      form.save()
      return redirect('pieza')
  else:
    form = PiezaForms()
    return render(request, 'componente_pieza/pieza.html',{'form':form})



def eliminarPieza(request, id_pieza):
  registro = get_object_or_404(Pieza, pk= id_pieza)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('pieza')
  
def editarPieza(request, id_pieza):
  sistema = get_object_or_404(Pieza, pk=id_pieza)
  form = PiezaForms(request.POST, instance=sistema)
  form.save()
  return redirect('pieza')

def obtenerDatos(request, id_pieza):
  pieza = list(Pieza.objects.filter(pk=id_pieza).values())
  if(len(pieza) > 0):
    data = {'mensaje': "Success", 'pieza': pieza}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
