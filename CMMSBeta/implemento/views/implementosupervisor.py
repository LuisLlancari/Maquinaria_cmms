from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import ImplementoSupervisor
from ..forms import ImplementoSupervisorForms
from django.http import JsonResponse
from django.contrib import messages


@login_required(login_url='login', redirect_field_name='')
def implementoSupervisor(request):
  datos = list(ImplementoSupervisor.objects.filter())
  contexto ={
    'datos':datos,
    'form':ImplementoSupervisorForms
  }
  return render(request, 'implemento/implementosupervisor.html', contexto)

@login_required(login_url='login', redirect_field_name='')
def registrarImplementoSupervisor(request):
  if request.method == 'POST':
    form = ImplementoSupervisorForms(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Se asigno un supervisor con éxito', extra_tags='success')
      return redirect('asignar_supervisor_implemento')

    else:
      return redirect('asignar_supervisor_implemento')

@login_required(login_url='login', redirect_field_name='')
def registrarFechaSalidaSupervisor(request, id_registro):
  if request.method == 'POST':
    print("holas")
    fechafin = request.POST.get('fechafin')
    registro = get_object_or_404(ImplementoSupervisor, pk = id_registro)
    print(registro.fechaFin)
    registro.fechaFin = fechafin
    registro.save()
    messages.success(request, 'Se asigno fecha de salida con éxito', extra_tags='primary')
    return redirect('asignar_supervisor_implemento')



@login_required(login_url='login', redirect_field_name='')
def eliminarImplementoSupervisor(request, id_registro):
  if request.method == 'POST':
    registro = get_object_or_404(ImplementoSupervisor, pk = id_registro)
    registro.estado = False
    registro.save()
    messages.success(request, 'Se elimino un registro con éxito', extra_tags='danger')
    return redirect('asignar_supervisor_implemento')
