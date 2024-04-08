from django.shortcuts import render
# importamos la libreria para que el logueo del usuario sea obligatorio
from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='home')
def home(request):
  return render(request, 'core/home.html')

@login_required(login_url='login', redirect_field_name='home')
def test(request):
  return render(request, 'core/test.html')