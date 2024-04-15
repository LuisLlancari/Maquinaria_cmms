from django.shortcuts import render, redirect, get_object_or_404
from ..models import Area, Base
from ..forms import AreaForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def area(request):
    areas = Area.objects.filter(estado = True)
    bases = Base.objects.filter(estado = True)
    formArea = AreaForm()
    datos = {
        'areas': areas,
        'formArea': formArea,
        'bases': bases
    }
    return render(request, '../templates/localizacion/area.html', datos)

@login_required(login_url='login', redirect_field_name='')
def eliminar_area(request, idarea):
    area = get_object_or_404(Area, pk = idarea)
    if request.method == 'POST':
        area.estado = False
        area.save()
        return redirect('area')
    
    return render(request, '', {'area': area})

@login_required(login_url='login', redirect_field_name='')
def registrar_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area')  # Redirige a la vista correcta para mostrar las bases registradas
    else:
        form = AreaForm()
        
    return render(request, '../templates/localizacion/area.html', {'form': form})

@login_required(login_url='login', redirect_field_name='')
def editar_area(request):
    if request.method == 'POST':
        idarea = request.POST.get('idarea')
        area = get_object_or_404(Area, pk=idarea)
        form = AreaForm(request.POST, instance=area)

        if form.is_valid():
            form.save()
            return redirect('area')
        else:
            # Obtener los errores del formulario
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")
