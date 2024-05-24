from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import DettaleConfiguracion
from django.http import JsonResponse

#Manejo de errores
from django.contrib import messages


def detalle_cong(request):
  lista_cong = DettaleConfiguracion.objects.filter(estado=True)
  contexto = {
    'lista_cong': lista_cong,
    'form': DettaleConfiguracion
  }
  return render(request, 'componente_pieza/detalle_cong.html', contexto)