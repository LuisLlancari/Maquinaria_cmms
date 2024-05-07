from django.shortcuts import render, redirect,get_object_or_404
from ..forms import UsuarioForm, RestablecerContraseña
from django.contrib.auth.forms import SetPasswordForm

from ..models import Usuario, Rol
from django.contrib import messages
from django.http import JsonResponse


def gestorUsuario(request):
  datos_usuarios = Usuario.objects.filter(is_active = True)
  return render(request, 'usuario/registro_usuario.html', {'form':UsuarioForm, 'usuarios':datos_usuarios, 'form2': RestablecerContraseña})

def registrarUsuario(request):
  datos_usuarios = Usuario.objects.filter(is_active = True)
  user_name = request.POST.get('username')

  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
        form.save()
        messages.error(request, 'Usuario registrado correctamente',extra_tags='success')
        return redirect('registro_usuario')
    else:
      messages.error(request, 'El usuario ya esta existe',extra_tags='success')
      return redirect('registro_usuario')
  else:
      return redirect('registro_usuario')

def editarUsuario(request, id_usuario):
  if request.method == 'POST':
    user_name = request.POST.get('username')
    user_rol = request.POST.get('idrol')
    user_firstname = request.POST.get('first_name') 
    user_lastname = request.POST.get('last_name') 

    usuario_actual = Usuario.objects.get(id=id_usuario)
    idrol = Rol.objects.get(idrol = user_rol)

    # Verificar si el nombre de usuario enviado es diferente al actual
    if user_name != usuario_actual.username:
        # Verificar si el nuevo nombre de usuario ya existe en la base de datos
        username_duplicado = Usuario.objects.filter(username=user_name).exists()
        
        if username_duplicado:
            # Si el nombre de usuario ya existe, mostrar un mensaje de error
            messages.error(request, 'El nombre de usuario ya está en uso',extra_tags='warning')
            return redirect('registro_usuario')
        
    # Actualizar los datos del usuario
    usuario_actual.username = user_name
    usuario_actual.idrol = idrol
    usuario_actual.first_name = user_firstname
    usuario_actual.last_name = user_lastname
    usuario_actual.save()

    messages.success(request, 'Usuario actualizado correctamente', extra_tags='success')
    return redirect('registro_usuario')
  else:
    return redirect('registro_usuario')

   
def eliminarUsuario(request, id_usuario):
  if request.method == 'POST':
    # Obtenemos el usuario a eliminar 
    usuario = Usuario.objects.get(id = id_usuario)
    # Desactivamos su estado y guardamos sus cambios
    usuario.is_active = False
    usuario.save()

    messages.error(request, 'Usuario eliminado',extra_tags='danger')
    return redirect('registro_usuario')
  else:
    return redirect('registro_usuario')


def restablecerContraseña(request, id_usuario):
  usuario = get_object_or_404(Usuario, pk=id_usuario) 
  if request.method == 'POST':
      form = RestablecerContraseña(usuario, request.POST)
      if form.is_valid():
          form.save()
          messages.error(request, 'Contraseña restablecida correctamente',extra_tags='success')
          return redirect('registro_usuario')
      else:
        messages.error(request, 'La contraseñas son diferentes',extra_tags='warning.')
        return redirect('registro_usuario')
  else:
      form = RestablecerContraseña(usuario)
      return render(request, 'usuario/registro_usuario.html', {'form': form})


def obtenerUsuario(request, id_usuario):
   usuario = list(Usuario.objects.filter(pk = id_usuario).values())
   data = {'usuarios': usuario}
   return JsonResponse(data)
    
