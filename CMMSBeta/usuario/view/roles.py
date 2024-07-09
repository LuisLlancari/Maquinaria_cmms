from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Rol
from ..forms import RolForm
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='')
def roles(request):
    rol = request.user.idrol.rol
    if rol == "Admin":
        roles = Rol.objects.filter(estado=True)
        form = RolForm()
        data = {
            'roles': roles,
            'form': form
        }
        return render(request, 'usuario/rol.html', data)
    else:
        return redirect('home')
    
@login_required(login_url='login', redirect_field_name='')
def eliminar_rol(request, idrol):
    if request.method == 'POST':
        rol = get_object_or_404(Rol, pk = idrol)
        rol.estado = False
        rol.save()
        messages.success(request, "El rol se ha eliminado correctamente", extra_tags='danger')
        return redirect('roles')
    
    
@login_required(login_url='login', redirect_field_name='')
def registrar_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)

        rol = request.POST.get('rol')
        print(rol)

        if Rol.objects.filter(rol= rol, estado = False).exists():
            rol_existente = get_object_or_404(Rol, rol=rol, estado=False)
            rol_existente.estado = True
            rol_existente.save()
            messages.success(request, "El rol se ha registrado correctamente", extra_tags='success')
            return redirect('roles')

        if form.is_valid():
            form.save()
            messages.success(request, "El rol se ha registrado correctamente", extra_tags='success')
            return redirect('roles')
        else:
            messages.success(request, "El rol ya existe", extra_tags='danger')
            return redirect('roles')

    else:
        return redirect('roles')

@login_required(login_url='login', redirect_field_name='')
def editar_rol(request):
    if request.method == 'POST':
        rol_id = request.POST.get('idrol')
        
        roles = get_object_or_404(Rol, pk = rol_id)
        form = RolForm(request.POST, instance = roles)

        if form.is_valid():
            form.save()
            messages.success(request, "El rol se ha registrado correctamente", extra_tags='success')
            return redirect('roles')
        else:
            messages.success(request, "El rol ya existe", extra_tags='danger')
            return redirect('roles')

    else:
        return redirect('roles')
   
    
    

        