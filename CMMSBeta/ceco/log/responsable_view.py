from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Responsable
@login_required(login_url='login', redirect_field_name='')
def responsable(request):
    responsable = Responsable.objects.filter(estado=True)
    return render(request, 'ceco/responsable.html',{'datos': responsable, 'form_responsable': ResponsableForm})

def registrar_responsable(request):
    form = ResponsableForm(request.POST)
    form.save()
    return redirect('responsable')

def eliminar_responsable(request, id_responsable):
    registro = get_object_or_404(Responsable, pk=id_responsable)
    if request.method == 'POST':
        registro.estado = False
        registro.save()
        return redirect('responsable')

def editar_responsable(request):
    if request.method == 'POST':
        responsable_id = request.POST.get('responsable_id')
        responsable_instance = get_object_or_404(Responsable, pk=responsable_id)
        form = ResponsableForm(request.POST, instance=responsable_instance)
        if form.is_valid():
            form.save()
            return redirect('responsable')
        else:
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue valida")