from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def fundo(request):
  return render(request, 'fundo_cultivo/fundo.html')

@login_required(login_url='login', redirect_field_name='')
def lote(request):
  return render(request, 'fundo_cultivo/lote.html')

@login_required(login_url='login', redirect_field_name='')
def variedad(request):
  return render(request, 'fundo_cultivo/variedad.html')

@login_required(login_url='login', redirect_field_name='')
def cultivo(request):
  return render(request, 'fundo_cultivo/cultivo.html')


# LOGICA FUNDO
