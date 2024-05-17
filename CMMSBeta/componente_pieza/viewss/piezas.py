from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from ..forms import SistemaForms
from django.http import JsonResponse


def piezas(request):
  return render(request, 'componente_pieza/piezas.html')