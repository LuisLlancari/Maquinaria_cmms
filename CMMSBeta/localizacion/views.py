from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='area')
def area(request):
    return render(request, 'localizacion/area.html')

@login_required(login_url='login', redirect_field_name='base')
def base(request):
    return render(request, 'localizacion/base.html')

@login_required(login_url='login', redirect_field_name='sede')
def sede(request):
    return render(request, 'localizacion/sede.html')
