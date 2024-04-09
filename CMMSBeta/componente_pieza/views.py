from django.shortcuts import render

# Create your views here.

def componente(request):
  return render(request, 'componente_pieza/componente.html')

def pieza(request):
  return render(request, 'componente_pieza/pieza.html')

def sistema(request):
  return render(request, 'componente_pieza/sistema.html')

