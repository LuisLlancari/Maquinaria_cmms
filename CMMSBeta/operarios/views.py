from django.shortcuts import render

def solicitante(request):
  return render(request, 'operarios/solicitante.html')

def tipoSolicitante(request):
  return render(request, 'operarios/tiposolicitante.html')

def tractoristas(request):
  return render(request, 'operarios/tractoristas.html')