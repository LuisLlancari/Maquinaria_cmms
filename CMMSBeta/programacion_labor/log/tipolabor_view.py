from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Tipolabor
@login_required(login_url='login', redirect_field_name='')
def tipolabor(request):
    tipolabor = TipoLabor.objects.filter(estado=True)
    return render(request, 'programacion_labor/tipolabor.html', {'datos': tipolabor, 'form_tipolabor': TipoLaborForm })

def registrar_tipolabor(request):
    form = TipoLaborForm(request.POST)
    form.save()
    return redirect('tipolabor')

def eliminar_tipolabor(request, id_tipolabor):
    registro = get_object_or_404(TipoLabor, pk=id_tipolabor)
    if request.method == 'POST':
        registro.estado = False
        registro.save()
        return redirect('tipolabor')
    
def editar_tipolabor(request):
    if request.method == 'POST':
        tipolabor_id = request.POST.get('tipolabor_id')
        tipolabor_instance = get_object_or_404(TipoLabor, pk=tipolabor_id)
        form = TipoLaborForm(request.POST, instance=tipolabor_instance)
        if form.is_valid():
            form.save()
            return redirect('tipolabor')
        else:
            # Obtener los errores del formulario
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")
