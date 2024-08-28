from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.contrib import messages
from usuario.forms import PersonaForm
from django.http import JsonResponse
from ..models import *  
from ..forms import *

@login_required(login_url='login', redirect_field_name='')
def responsable(request):
    responsable = Encargado.objects.filter(estado = True)
    contexto = {
        'datos': responsable,
        'form': PersonaForm
    }
    return render(request, 'operarios/encargado.html', contexto)

@login_required(login_url='login', redirect_field_name='')
def registrar_responsable(request):
    if request.method == 'POST':
        encargado_Form = PersonaForm(request.POST)
        if encargado_Form.is_valid():
            encargado_Form.save()

            ultimo_registro = Persona.objects.latest('idpersona')
            id_persona = ultimo_registro.idpersona

            persona = Persona.objects.get(pk=id_persona)

            Encargado.objects.create(idpersona = persona)

            messages.success(request, 'Tractorista registrado con exito', extra_tags='success')
            return redirect('responsable')
        else:
            messages.success(request, 'El DNI ya existe', extra_tags='danger')
            return redirect('responsable')

@login_required(login_url='login', redirect_field_name='')
def eliminar_responsable(request, id_encargado):
    if request.method == 'POST':
        encargado = get_object_or_404(Encargado, pk=id_encargado)
        encargado.estado = False
        encargado.save()
        return redirect('responsable')

@login_required(login_url='login', redirect_field_name='')
def editar_responsable(request, id_encargado):
    if request.method == 'POST':
        encargado = get_object_or_404(Encargado, idencargado = id_encargado)
        id_persona = encargado.idpersona.idpersona
        persona = get_object_or_404(Persona, idpersona = id_persona)
        
        formPersona = PersonaForm(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
            messages.success(request, 'Encargado editado con exito', extra_tags='primary')
            return redirect('responsable')
        else:
            messages.success(request, 'El DNI ya existe', extra_tags='danger')
            return redirect('responsable')
        pass

@login_required(login_url='login', redirect_field_name='')
def obtenerDatos(request, id_encargado):
    encargado = get_object_or_404(Encargado, idencargado=id_encargado)

    datos = {
        'encargado': {
            'nombres': encargado.idpersona.nombres,
            'apellidos': encargado.idpersona.apellidos,
            'dni': encargado.idpersona.dni,
        }
    }

    return JsonResponse(datos)