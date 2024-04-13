from django.shortcuts import render, redirect, get_object_or_404
from ..models import Base
from ..forms import BaseForm

def base(request):
    bases = Base.objects.all()
    formBase = BaseForm()
    datos = {
        'bases': bases,
        'formBase': formBase,
    }
    return render(request, '../templates/localizacion/base.html', datos)

def eliminar_base(request, idbase):
    base = get_object_or_404(Base, pk = idbase)
    if request.method == 'POST':
        base.delete()
        return redirect('base')
    
    return render(request, '', {'sede': base})

def registrar_base(request):
    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')  # Redirige a la vista correcta para mostrar las bases registradas
    else:
        form = BaseForm()
        
    return render(request, '../templates/localizacion/base.html', {'form': form})

def editar_base(request):
    if request.method == 'POST':
        idbase = request.POST.get('idarea')
        base = get_object_or_404(Base, pk = idbase)
        form = BaseForm(request.POST, instance=base)

        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        return redirect('base')

    return render(request, '../templates/localizacion/base.html', {'form': form})

