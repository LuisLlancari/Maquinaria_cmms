from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Implemento
from ..forms import ImplementoForms
from django.http import JsonResponse


#Manejo de errores
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='implemento')
def implemento(request):
  # Obtenemos el Rol y ID del usuario 
  rol_usuario = request.user.idrol.rol
  id_usuario = request.user.id

  # Comparamos el Rol 
  if rol_usuario == "Supervisor":
    datos_implemento = Implemento.objects.filter(estado = True, idusuario = id_usuario)
    return render(request, 'implemento/implemento.html', {'datos': datos_implemento, 'form':ImplementoForms})

  else:
    datos_implemento = Implemento.objects.filter(estado = True) 
    return render(request, 'implemento/implemento.html', {'datos': datos_implemento, 'form':ImplementoForms})

def registrarImplemento(request):
  if request.method == 'POST':
    nom_implemento = request.POST.get('implemento').strip()
    cod_implemento = request.POST.get('codimplemento').strip()
    existe_nom = Implemento.objects.filter(implemento = nom_implemento, estado = True).exists()
    existe_cod = Implemento.objects.filter(codimplemento = cod_implemento, estado = True).exists()
    form = ImplementoForms(request.POST)
    if form.is_valid() and existe_nom == False and existe_cod == False:
      form.save()
      messages.success(request, 'Implemento registrado con exito', extra_tags='success')
      return redirect('implemento')
    
      
    else:
      messages.error(request, 'El implemento ya existe', extra_tags='danger')
  return redirect('implemento')

def eliminarimplemento(request, id_implemento):
  registro = get_object_or_404(Implemento, pk= id_implemento)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('implemento')
  
def editarImplemento(request, id_implemento):
  if request.method == 'POST':
    implemento = get_object_or_404(Implemento, pk=id_implemento)
    form = ImplementoForms(request.POST, instance=implemento)
    nom_implemento = request.POST.get('implemento').strip()
    cod_implemento = request.POST.get('codimplemento').strip()
    #existe_nom = Implemento.objects.filter(implemento = nom_implemento, estado = True).exists()
    #existe_cod = Implemento.objects.filter(codimplemento = cod_implemento, estado = True).exists()
    if form.is_valid():
      form.save()
      messages.success(request, 'Implemento editado con exito', extra_tags='primary')
      return redirect('implemento')
    else:
      messages.error(request, 'El implemento ya existe', extra_tags='danger')
      return redirect('implemento')
  return redirect('implemento')

def obtenerDatos(request, id_implemento):
  implemento = list(Implemento.objects.filter(pk=id_implemento).values())
  if(len(implemento) > 0):
    data = {'mensaje': "Success", 'implemento': implemento}
  else:
    data = {'mensaje':"Not found"}
  return JsonResponse(data)
