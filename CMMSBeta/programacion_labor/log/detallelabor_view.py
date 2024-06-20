from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Detallelabor
@login_required(login_url='login', redirect_field_name='')
def detallelabor(request):
    rol = request.user.idrol.rol
    if rol == "Admin":
        detallelabor = DetalleLabor.objects.filter(estado=True)
        return render(request, 'programacion_labor/detallelabor.html', {'datos': detallelabor, 'form_detallelabor': DetalleLaborForm })
    else:
        return redirect('home')