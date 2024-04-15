from django.shortcuts import render, redirect, get_object_or_404
from ..models import Base
from ..forms import BaseForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def base(request):
    bases = Base.objects.filter(estado = True)
    formBase = BaseForm()
    datos = {
        'bases': bases,
        'formBase': formBase,
    }
    return render(request, '../templates/localizacion/base.html', datos)

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
            form.save()
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
            form.save()
            return redirect('base')
    else:
        return redirect('base')

    return render(request, '../templates/localizacion/base.html', {'form': form})

