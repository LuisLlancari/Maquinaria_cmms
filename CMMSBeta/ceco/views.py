from django.shortcuts import render, redirect, get_object_or_404
from .models import Ceco
from .forms import CecoForm
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def ceco(request):
    cecos = Ceco.objects.all()
    for ceco in cecos:
        #MANEJO DE ESTADO
        ceco.estado = 'Activo' if ceco.estado else 'Inactivo'
    return render(request, 'ceco/ceco.html', {'datos': cecos, 'form': CecoForm})

@login_required(login_url='login', redirect_field_name='')
def registrar_ceco(request):
    form = CecoForm(request.POST)
    form.save()
    return redirect('ceco')


@login_required(login_url='login', redirect_field_name='')
def editar_ceco(request):
    if request.method == 'POST':
        ceco_id = request.POST.get('ceco_id')
        ceco_instance = get_object_or_404(Ceco, pk=ceco_id)
        form = CecoForm(request.POST, instance=ceco_instance)
        if form.is_valid():
            form.save()
            return redirect('ceco')
        else:
            # Obtener los errores del formulario
            errores = form.errors.as_text()
            mensaje_error = f"Hubo un error en el formulario: {errores}"
            return HttpResponse(mensaje_error)
    else:
        return HttpResponse("La solicitud no fue válida")














@login_required(login_url='login', redirect_field_name='')
def responsable(request):
    return render(request, 'ceco/responsable.html')