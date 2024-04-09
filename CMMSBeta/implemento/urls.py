from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from . import views

urlpatterns = [
  path('', views.implento , name='implemento'),
  path('tipos', views.tipoImplemento , name='tipoimplemento'),
  path('detalle', views.detalleImplemento   , name='detalleimplemento'),
]
