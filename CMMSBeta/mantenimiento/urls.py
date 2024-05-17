from django.urls import path, include
from .views import horauso

urlpatterns = [
  path('', horauso.horasuso, name= "horas_uso" ),
]