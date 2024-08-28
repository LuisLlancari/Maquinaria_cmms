from django.shortcuts import render, redirect, get_object_or_404
from ..models import Area, Base
from ..forms import AreaForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def area(request):
    rol = request.user.idrol.rol
    if rol == "Admin":
        areas = Area.objects.filter(estado = True)
        bases = Base.objects.filter(estado = True)
        formArea = AreaForm()
        datos = {
            'areas': areas,
            'formArea': formArea,
            'bases': bases
        }
        return render(request, '../templates/localizacion/area.html', datos)
    else:
        return redirect('home')
    
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
            nombre_area = form.cleaned_data['area']
            id_base = request.POST.get('idbase')
            if Area.objects.filter(idbase = id_base, area= nombre_area, estado = True).exists():
                messages.success(request, "El area ya existe", extra_tags='warning')
                return redirect('area') 
            else:    
                messages.success(request, "El area ha sido agregada correctamente", extra_tags='success')
                form.save()
                return redirect('area') 
        else:
            messages.success(request, "Ingrese informacion válida", extra_tags='danger')
            return redirect('area')           
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
            nombre_area = form.cleaned_data['area']
            id_base = request.POST.get('idbase')
            
            if Area.objects.filter(idbase = id_base, area= nombre_area, estado = True).exists():
                messages.success(request, "El area ya existe", extra_tags='warning')
                return redirect('area') 
            else:
                form.save()
                messages.success(request, "El registro ha sido modificado correctamente", extra_tags='primary')
            return redirect('area')
        else:
            # Obtener los errores del formulario
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")
