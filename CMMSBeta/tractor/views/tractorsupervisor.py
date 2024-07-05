from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import TractorSupervisor
from ..forms import TractorSupervisorForms
from django.http import JsonResponse
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='')
def tractorSupervisor(request):
  datos = list(TractorSupervisor.objects.filter(estado = True))
  contexto ={
    'datos':datos,
    'form':TractorSupervisorForms
  }
  return render(request, 'tractor/tractorsupervisor.html', contexto)

@login_required(login_url='login', redirect_field_name='')
def registrartractorSupervisor(request):
  if request.method == 'POST':
    form = TractorSupervisorForms(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Se asigno un supervisor con éxito', extra_tags='success')
      return redirect('asignar_supervisor_tractor')

    else:
      return redirect('asignar_supervisor_tractor')

@login_required(login_url='login', redirect_field_name='')
def registrarFechaSalidaSupervisor(request, id_registro):
  if request.method == 'POST':
    print("holas")
    fechafin = request.POST.get('fechafin')
    registro = get_object_or_404(TractorSupervisor, pk = id_registro)
    print(registro.fechaFin)
    registro.fechaFin = fechafin
    registro.save()
    messages.success(request, 'Se asigno fecha de salida con éxito', extra_tags='primary')
    return redirect('asignar_supervisor_tractor')



@login_required(login_url='login', redirect_field_name='')
def eliminartractorSupervisor (request, id_registro):
  if request.method == 'POST':
    registro = get_object_or_404(TractorSupervisor, pk = id_registro)
    registro.estado = False
    registro.save()
    messages.success(request, 'Se elimino un registro con éxito', extra_tags='danger')
    return redirect('asignar_supervisor_tractor')
