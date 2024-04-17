from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from ..models import TipoTractor,Tractor
from ..forms import TipoTractorForm

#VERIFICA SI EL USUARIO ESTA LOGUEADO

@login_required(login_url='login', redirect_field_name='tipotractor')
def tipotractor(request):
    tipotractor = TipoTractor.objects.filter(estado = True)
    form = TipoTractorForm()
    data = {
        'tipotractor' : tipotractor,
        'form' : form
    }
    return render(request, 'tractor/tipotractor.html', data)

@login_required(login_url='login', redirect_field_name='tipotractor')
def eliminar_tipotractor(request, idtractor):
    tipotractor = get_object_or_404(TipoTractor, pk=idtractor)
    if request.method == 'POST':
        tipotractor.estado = False
        tipotractor.save()
        
        tractor_relacionadas = Tractor.objects.filter(idtipotractor=idtractor)
        for tractor in tractor_relacionadas:
            tractor.estado = False
            tractor.save()
        return redirect('tipotractor')
    
    return render(request, '', {'tipotractor': tipotractor})

@login_required(login_url='login', redirect_field_name='')
def registrar_tipotractor(request):
    if request.method == 'POST':
        form = TipoTractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipotractor')
    else:
        form = TipoTractorForm()
        return render(request, '', {'form': form})
    
@login_required(login_url='login', redirect_field_name='')
def editar_tipo(request):
    if request.method == 'POST':
        idtipo = request.POST.get('idtipotractor')
        tipo = get_object_or_404(TipoTractor, pk = idtipo)
        form = TipoTractorForm(request.POST, instance=tipo)

        if form.is_valid():
            form.save()
            return redirect('tipotractor')
    else:
        return redirect('editartipo')

    return render(request, '', {'form': form})
