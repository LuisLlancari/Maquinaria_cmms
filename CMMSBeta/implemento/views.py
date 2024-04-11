from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import TipoImplemento, Implemento, DetImplementos

# verifica si el usuario esta logueado
@login_required(login_url='login', redirect_field_name='implemento')
# definimos la vista
def implento(request):
  

  # retornamos el render de la plantilla de nuestra vista
  return render(request, 'implemento/implemento.html')

def tipoImplemento (request):
  datos_tipoimplemento = TipoImplemento.objects.filter(estado = True   )
  return render(request, 'implemento/tipoimplemento.html')

def detalleImplemento (request):
  return render(request, 'implemento/detalleimplemento.html')