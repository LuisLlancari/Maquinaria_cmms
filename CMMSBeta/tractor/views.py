from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#VERIFICA SI EL USUARIO ESTA LOGUEADO
@login_required(login_url='login', redirect_field_name='tractor')
#DEFINIMOS LA VISTA
def reportetractor(request):
    return render(request, 'tractor/reportetractor.html')

@login_required(login_url='login', redirect_field_name='tipotractor')
def tipotractor(request):
    return render(request, 'tractor/tipotractor.html')

@login_required(login_url='login', redirect_field_name='localizacion')
def tractor(request):
    return render(request, 'tractor/tractor.html')
