from django.shortcuts import render, redirect
from ..forms import UsuarioForm
from ..models import Usuario
from django.contrib import messages

def gestorUsuario(request):
  datos_usuarios = Usuario.objects.all()
  return render(request, 'usuario/registro_usuario.html', {'form':UsuarioForm, 'usuarios':datos_usuarios})

def registrarUsuario(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('registro_usuario')
  else:
    form = UsuarioForm()
    
    # Si el formulario no es válido, se pasa nuevamente al contexto
    # para que los errores puedan mostrarse en el template
  if not form.is_valid() and request.method == 'POST':
        return render(request, 'usuario/registro_usuario.html', {'form': form})
    
  return render(request, 'usuario/registro_usuario.html', {'form': form})