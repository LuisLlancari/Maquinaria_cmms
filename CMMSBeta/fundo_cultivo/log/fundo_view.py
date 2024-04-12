from django.shortcuts import render, redirect, get_object_or_404
from ..models import *  
from ..forms import *
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='login', redirect_field_name='')
def fundo(request):
  return render(request, 'fundo_cultivo/fundo.html')