from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from ..models import ReporteTractor, TipoTractor
from ..forms import ReporteTractorForm

@login_required(login_url='login', redirect_field_name='')
def reportetractor(request):
    reporte = ReporteTractor.objects.filter(estado = True)
    usuario = request.user
    form = ReporteTractorForm()
    data = {
        'reportes' : reporte,
        'usuario' : usuario
    }
    return render(request, 'tractor/reportetractor.html', data)
