from django.shortcuts import render, redirect, get_object_or_404
from ..models import Componente
from ..forms import ComponenteForms
from django.http import JsonResponse

def componente(request):
  datos_componente = Componente.objects.filter(estado =True)
  return render(request, 'componente_pieza/componente.html',{'datos_componente':datos_componente, 'form':ComponenteForms})

def registrarComponente(request):
  if request.method == 'POST':
      form = ComponenteForms(request.POST)
      if form.is_valid():  # Verifica si los datos son válidos
          form.save()
          return redirect('componente')
  else:
      form = ComponenteForms()
  
  return render(request, 'componente_pieza/componente.html', {'form': form})

def eliminarComponente(request, id_componente):
  registro = get_object_or_404(Componente, pk= id_componente)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
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