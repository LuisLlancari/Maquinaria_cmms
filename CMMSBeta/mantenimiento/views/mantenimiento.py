from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento
from django.http import JsonResponse

def mantenimientos_realizados(request):
  return render(request, 'mantenimiento/completar_programaciones.html')