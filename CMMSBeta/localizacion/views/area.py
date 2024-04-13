from django.shortcuts import render, redirect, get_object_or_404
from ..models import Area
from ..forms import AreaForm

def area(request):
    areas = Area.objects.all()
    formArea = AreaForm()
    datos = {
        'areas': areas,
        'formArea': formArea,
    }
    return render(request, '../templates/localizacion/area.html', datos)

def eliminar_area(request, idarea):
    area = get_object_or_404(Area, pk = idarea)
    if request.method == 'POST':
        area.delete()
        return redirect('area')
    
    return render(request, '', {'area': area})

def registrar_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area')  # Redirige a la vista correcta para mostrar las bases registradas
    else:
        form = AreaForm()
        
    return render(request, '../templates/localizacion/area.html', {'form': form})

def editar_area(request):
    if request.method == 'POST':
        idarea = request.POST.get('idarea')
        area = get_object_or_404(Area, pk=idarea)
        form = AreaForm(request.POST, instance=area)

        if form.is_valid():
            form.save()
            return redirect('area')
    else:
        return redirect('area')

    return render(request, '../templates/localizacion/area.html', {'form': form})