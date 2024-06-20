from django.shortcuts import render, redirect, get_object_or_404
from ..models import Base, Sede
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import BaseForm

@login_required(login_url='login', redirect_field_name='')
def base(request):
    rol = request.user.idrol.rol
    if rol == "Admin":
        bases = Base.objects.filter(estado = True)
        sedes = Sede.objects.filter(estado = True)
        formBase = BaseForm()
        datos = {
            'bases': bases,
            'formBase': formBase,
            'sedes':sedes,
        }
        return render(request, '../templates/localizacion/base.html', datos)
    else:
        return redirect('home')
    

@login_required(login_url='login', redirect_field_name='')
def eliminar_base(request, idbase):
    base = get_object_or_404(Base, pk = idbase)
    if request.method == 'POST':
        base.estado = False
        base.save()     
        return redirect('base')
    
    return render(request, '', {'sede': base})

@login_required(login_url='login', redirect_field_name='')
def registrar_base(request):
    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            # Obtenemos datos del formulario
            base_nombre = form.cleaned_data['base']
            id_sede = request.POST.get('idsede')

            if Base.objects.filter(idsede = id_sede ,base = base_nombre , estado = True).exists():
                messages.success(request, "La Base ya existe", extra_tags='warning')
            else:
                form.save()
                messages.success(request, "La base ha sido agregada correctamente", extra_tags='success')
            return redirect('base')  
        else:
            messages.success(request, "Ingrese información válida", extra_tags='danger')
            return redirect('base')
    else:
        form = BaseForm()     
        return render(request, '../templates/localizacion/base.html', {'form': form})

@login_required(login_url='login', redirect_field_name='')
def editar_base(request):
    if request.method == 'POST':
        idbase = request.POST.get('idbase')
        base = get_object_or_404(Base, pk = idbase)
        form = BaseForm(request.POST, instance=base)

        if form.is_valid():
            base_nombre = form.cleaned_data['base']
            id_sede = request.POST.get('idsede')

            if Base.objects.filter(idsede = id_sede ,base = base_nombre, estado = True).exists():
                messages.success(request, "La Base ya existe", extra_tags='warning')
                return redirect('base')
            else:
                form.save()
                messages.success(request, "El registro ha sido modificado correctamente", extra_tags='primary')
                return redirect('base')
        
        else:
            messages.success(request, "Ingrese información válida", extra_tags='danger')
            return redirect('base')    
    else:
        return redirect('base')

   

