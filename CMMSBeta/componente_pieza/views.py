from django.shortcuts import render, redirect, get_object_or_404
from .models import Sistema, Componente, Pieza
from .forms import SistemaForms

def componente(request):
  return render(request, 'componente_pieza/componente.html')

def pieza(request):
  return render(request, 'componente_pieza/pieza.html')

def sistema(request):
  datos_sistema = Sistema.objects.filter(estado=True)
  return render(request, 'componente_pieza/sistema.html',{'datos_sistema':datos_sistema, 'form':SistemaForms})

def registrarSistema(request):
  form = SistemaForms(request.POST)
  form.save()
  return redirect('sistema')

def eliminarSistema(request, id_sistema):
  registro = get_object_or_404(Sistema, pk= id_sistema)
  if request.method == 'POST':
    registro.estado = False
    registro.save()
    return redirect('sistema')

def editarSistema(request, id_sistema):
  pass