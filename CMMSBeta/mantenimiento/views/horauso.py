from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def horasuso(request):
  
  return render(request, 'mantenimiento/horasdeuso.html' )