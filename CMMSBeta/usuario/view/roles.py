from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Rol
from ..forms import RolForm

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
        return render(request, '../templates/usuario/rol.html', data)
    else:
        return redirect('home')
    
@login_required(login_url='login', redirect_field_name='')
def eliminar_rol(request, idrol):
    rol = get_object_or_404(Rol, pk = idrol)
    if request.method == 'POST':
        rol.estado = False
        rol.save()
        return redirect('roles')
    
    return render(request, '../templates/usuario/rol.html', {'rol': rol})

@login_required(login_url='login', redirect_field_name='')
def registrar_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roles')
    else:
        form = RolForm()
        return render(request, '../templates/usuario/rol.html', {'form': form})

@login_required(login_url='login', redirect_field_name='')
def editar_rol(request):
    if request.method == 'POST':
        rol_id = request.POST.get('idrol')
        
        roles = get_object_or_404(Rol, pk = rol_id)
        form = RolForm(request.POST, instance = roles)

        if form.is_valid():
            form.save()
            return redirect('roles')

    else:
        return redirect('roles')

    return render(request, '', {'formeditar': form})
    
    
    

        