from django.urls import path
from . import views

urlpatterns = [
  path('fundo', views.fundo , name='fundo'),
  path('cultivo', views.cultivo , name='cultivo'),
  path('variedad', views.variedad , name='variedad'),
  path('lote', views.lote , name='lote'),
]