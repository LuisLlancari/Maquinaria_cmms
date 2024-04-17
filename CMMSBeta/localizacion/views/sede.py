from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sede, Base, Area
from ..forms import SedeForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def sede(request):
    sedes = Sede.objects.filter(estado = True)
    form = SedeForm()
    return render(request, '../templates/localizacion/sede.html', {'sedes': sedes, 'form': form})


@login_required(login_url='login', redirect_field_name='')
def eliminar_sede(request, idsede):
    sede = get_object_or_404(Sede, pk=idsede)
    
    # Cambiar el estado de la sede a False
    sede.estado = False
    sede.save()
    
    # Cambiar el estado de las bases relacionadas a False
    sede_relacionadas = Base.objects.filter(idsede=idsede)
    for base in sede_relacionadas:
        base.estado = False
        base.save()
    
    return redirect('sede')

@login_required(login_url='login', redirect_field_name='')
def registrar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sede')
    else:
        form = SedeForm()
        return render(request, '../templates/localizacion/sede.html', {'form': form})

@login_required(login_url='login', redirect_field_name='')
def editar_sede(request):
    if request.method == 'POST':
        sede_id = request.POST.get('idsede')

        sede = get_object_or_404(Sede, pk=sede_id)
        form = SedeForm(request.POST, instance=sede)

        if form.is_valid():
            form.save()
            return redirect('sede')

    else:
        return redirect('sede')

    return render(request, '', {'form': form})
