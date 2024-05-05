from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Tractor, TipoTractor
from ..forms import TractorForm
from django.contrib import messages
from fundo_cultivo.models import Fundo
from usuario.models import Usuario

@login_required(login_url='login', redirect_field_name='')
def tractor(request):

    rol_usuario = request.user.idrol.rol
    id_usuario = request.user.id
    if rol_usuario == "Supervisor":
        tractores = Tractor.objects.filter(estado = True , idusuario = id_usuario)
        tipotractor = TipoTractor.objects.filter(estado = True)
        fundo = Fundo.objects.filter(estado = True)
        usuario = Usuario.objects.filter(idrol = 3) 
        form = TractorForm()
        data = {
            'tractores' : tractores,
            'form' : form,
            'tipotractor' : tipotractor,
            'fundo' : fundo,
            'usuario' : usuario
        }
        
        return render(request, 'tractor/tractor.html', data)
    
    else:
        tractores = Tractor.objects.filter(estado = True)
        tipotractor = TipoTractor.objects.filter(estado = True)
        fundo = Fundo.objects.filter(estado = True)
        usuario = Usuario.objects.filter(idrol = 3) 
        form = TractorForm()
        data = {
            'tractores' : tractores,
            'form' : form,
            'tipotractor' : tipotractor,
            'fundo' : fundo,
            'usuario' : usuario
        }
        
        return render(request, 'tractor/tractor.html', data)


@login_required(login_url='login', redirect_field_name='')
def eliminar_tractor(request, idtractor):
    tractor = get_object_or_404(Tractor, pk = idtractor)
    if request.method == 'POST':
        tractor.estado = False
        tractor.save()
        return redirect('tractor')
    
@login_required(login_url='login', redirect_field_name='')
def registrar_tractor(request):
    if request.method == 'POST':
        form = TractorForm(request.POST)
        nom_tractor = request.POST.get('nrotractor').strip()
        existe_tractor = Tractor.objects.filter(nrotractor = nom_tractor, estado = True).exists()
        if form.is_valid() and existe_tractor == False:
            form.save()
            messages.success(request, "El tractor ha sido agregado correctamente", extra_tags='success')
            return redirect('tractor')
        else:
            messages.success(request, "El tractor ya existe", extra_tags='warning')
            return redirect('tractor')
    else:
        return redirect('tractor')
    
@login_required(login_url='login', redirect_field_name='')
def editar_tractor(request):
    if request.method == 'POST':
        idtractor = request.POST.get('idtractor')
        tractor = get_object_or_404(Tractor, pk = idtractor)
        form = TractorForm(request.POST, instance=tractor)

        nom_tractor = request.POST.get('nrotractor').strip()
        existe_tractor = Tractor.objects.filter(nrotractor = nom_tractor, estado = True).exists()
        if form.is_valid() and existe_tractor == False:
            form.save()
            messages.success(request, "El tractor ha sido modificado correctamente", extra_tags='primary')
            return redirect('tractor')
        else:
            messages.success(request, "El tractor ya existe", extra_tags='warning')
            return redirect('tractor')
    else:
        return redirect('tractor')




    

    


