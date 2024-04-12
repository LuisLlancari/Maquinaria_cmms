from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Sede
from ..forms import SedeForm

@login_required(login_url='login')
def area(request):
    return render(request, 'localizacion/area.html')

@login_required(login_url='login')
def base(request):
    return render(request, 'localizacion/base.html')

@login_required(login_url='login')
def sedeall(request):
    sedes = Sede.objects.all()
    return render(request, 'localizacion/sede.html', {'sedes': sedes})




@login_required(login_url='login')
def registrar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sede')
    else:
        form = SedeForm()

    return render(request, 'localizacion/registrar_sede.html', {'form': form})

@login_required(login_url='login')
def eliminar_sede(request, sede_id):
    sede = get_object_or_404(Sede, pk=sede_id)
    
    if request.method == 'POST':
        sede.delete()
        return redirect('sede')
    
    return render(request, 'localizacion/confirmar_eliminacion.html', {'sede': sede})

@login_required(login_url='login')
def editar_sede(request, sede_id):
    sede_instance = get_object_or_404(Sede, pk=sede_id)
    
    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede_instance)
        if form.is_valid():
            form.save()
            return redirect('sede')
    else:
        form = SedeForm(instance=sede_instance)
    
    return render(request, 'localizacion/editar_sede.html', {'form': form})





  
    