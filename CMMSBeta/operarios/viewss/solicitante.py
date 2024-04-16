from django.shortcuts import render, redirect, get_object_or_404
from ..models import Solicitante
from ..forms import SolicitanteForms
from django.http import JsonResponse

def solicitante(request):
  datos_solicitantes = Solicitante.objects.filter(estado=True)
  return render(request, 'operarios/solicitante.html', {'datos_solicitantes': datos_solicitantes, 'form':SolicitanteForms})

def registrarSolicitante(request):
  datos_solicitantes = Solicitante.objects.filter(estado=True)

  if request.method == 'POST':
    form = SolicitanteForms(request.POST)
    if form.is_valid():  # Verifica si los datos son válidos
      form.save()
      return redirect('solicitante')
  else:
     return render(request, 'operarios/solicitante.html', {'datos_solicitantes': datos_solicitantes})


def eliminarSolicitante(request, id_componente):
  registro = get_object_or_404(Solicitante, pk= id_componente)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('solicitante')
  
def editarSolicitante(request, id_solicitante):
  solicitante = get_object_or_404(Solicitante, pk=id_solicitante)
  form = SolicitanteForms(request.POST, instance=solicitante)
  form.save()
  return redirect('solicitante')

def obtenerDatos(request, id_solicitante):
  solicitante = list(Solicitante.objects.filter(pk=id_solicitante).values())
  if(len(solicitante) > 0):
    data = {'mensaje': "Success", 'solicitante': solicitante}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)