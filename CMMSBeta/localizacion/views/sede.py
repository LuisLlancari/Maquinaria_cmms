from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sede
from ..forms import SedeForm

def sede(request):
    sedes = Sede.objects.all()
    return render(request, '../templates/localizacion/sede.html', {'sedes': sedes})

        