from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from ..models import ReporteTractor
from ..forms import ReporteTractorForm

@login_required(login_url='login', redirect_field_name='')
def reportetractor(request):
    reporte = ReporteTractor.objects.filter(estado = True)
    form = ReporteTractorForm()
    data = {
        'reporte' : reporte,
        'form' : form
    }
    return render(request, 'tractor/reportetractor.html', data)


@login_required(login_url='login', redirect_field_name='')
def eliminar_reporte(request, idreporte):
    reportetractor = get_object_or_404(ReporteTractor, pk=idreporte)
    if request.method == 'POST':
        reportetractor.estado = False
        reportetractor.save()
        return redirect('reportetractor')
    
    return render(request, 'tractor/reportetractor.html', {'reporte': reportetractor})

@login_required(login_url='login', redirect_field_name='')
def registrar_reporte(request):
    if request.method == 'POST':
        form = ReporteTractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reportetractor')
    else:
        form = ReporteTractorForm()
        return render(request, 'tractor/reportetractor.html', {'form': form})
@login_required(login_url='login', redirect_field_name='')
def editar_reporte(request):
    if request.method == 'POST':
        idreporte = request.POST.get('idtipo')
        reporte = get_object_or_404(ReporteTractor, pk = idreporte)
        form = ReporteTractorForm(request.POST, instance=reporte)

        if form.is_valid():
            form.save()
            return redirect('reportetractor')
    else:
        return redirect('reportetractor')

    return render(request, '', {'form': form})
