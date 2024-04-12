from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sede
from ..forms import SedeForm

def sede(request):
    sedes = Sede.objects.all()
    form = SedeForm()
    return render(request, '../templates/localizacion/sede.html', {'sedes': sedes, 'form': form})

def eliminar_sede(request, idsede):
    sede = get_object_or_404(Sede, pk = idsede)
    if request.method == 'POST':
        sede.delete()
        return redirect('sede')
    
    return render(request, '', {'sede': sede})

def registrar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sede')
    else:
        form = SedeForm()
        return render(request, 'localizacion/registrar_sede.html', {'form': form})
    
    
    
    

        