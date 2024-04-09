from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# verifica si el usuario esta logueado
@login_required(login_url='login', redirect_field_name='')
# definimos la vista
def implento(request):
  # retornamos el render de la plantilla de nuestra vista
  return render(request, 'implemento/implemento.html')