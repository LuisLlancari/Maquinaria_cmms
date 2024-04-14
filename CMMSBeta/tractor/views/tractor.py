from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Tractor
from ..forms import TractorForm

def tractor(request):
    tractores = Tractor.objects.filter(estado = True)
    form = TractorForm()
    data = {
        'tractores' : tractores,
        'form' : form
    }
    
    return render(request, 'tractor/tractor.html', data)

def eliminar_tractor(request, idtractor):
    tractor = get_object_or_404(Tractor, pk = idtractor)
    if request.method == 'POST':
        tractor.estado = False
        tractor.save()
        return redirect('tractor')
    
def registrar_tractor(request):
    if request.method == 'POST':
        form = TractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tractor')
    else:
        form = TractorForm()
        return render(request, '', {'form': form})
    
def editar_tractor(request):
    if request.method == 'POST':
        idtractor = request.POST.get('idtractor')
        tractor = get_object_or_404(Tractor, pk = idtractor)
        form = TractorForm(request.POST, instance=tractor)

        if form.is_valid():
            form.save()
            return redirect('tractor')
    else:
        return redirect('tractor')

    return render(request, 'tractor/tractor.html', {'form': form})



    

    


