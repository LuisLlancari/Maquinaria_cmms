from django.shortcuts import render, redirect, get_object_or_404
from .models import Sistema, Componente, Pieza
from .forms import SistemaForms

def componente(request):
  datos_componente = Componente.objects.filter(estado =True)
  return render(request, 'componente_pieza/componente.html',{'datos_componente':datos_componente})

def pieza(request):
  datos_pieza = Pieza.objects.filter(estado=True)
  return render(request, 'componente_pieza/pieza.html',{'datos_pieza':datos_pieza})

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

def editarSistema(request):
    if request.method == 'POST':
        ceco_id = request.POST.get('ceco_id')
        ceco_instance = get_object_or_404(Ceco, pk=ceco_id)
        form = CecoForm(request.POST, instance=ceco_instance)
        if form.is_valid():
            form.save()
            return redirect('ceco')
        else:
            # Obtener los errores del formulario
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")