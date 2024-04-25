from django.shortcuts import render, redirect, get_object_or_404
#from ..models import *  
#from ..forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max , Count, Subquery, OuterRef
from implemento.models import *
from django.http import JsonResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
def mantenimiento(request):
    return render(request, 'mantenimiento/mantenimiento.html')