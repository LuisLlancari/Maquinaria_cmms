from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Implemento
from ..forms import ImplementoForms
from django.http import JsonResponse


@login_required(login_url='login', redirect_field_name='implemento')
def implemento(request):
  datos_implemento = Implemento.objects.filter(estado = True) 
  return render(request, 'implemento/implemento.html', {'datos': datos_implemento, 'form':ImplementoForms})

def registrarImplemento(request):
  form = ImplementoForms(request.POST)
  form.save()
  return redirect('implemento')

def eliminarimplemento(request, id_implemento):
  registro = get_object_or_404(Implemento, pk= id_implemento)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('implemento')
  
def editarImplemento(request, id_implemento):
  implemento = get_object_or_404(Implemento, pk=id_implemento)
  form = ImplementoForms(request.POST, instance=implemento)
  form.save()
  return redirect('implemento')


def obtenerDatos(request, id_implemento):
  implemento = list(Implemento.objects.filter(pk=id_implemento).values())
  if(len(implemento) > 0):
    data = {'mensaje': "Success", 'implemento': implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
