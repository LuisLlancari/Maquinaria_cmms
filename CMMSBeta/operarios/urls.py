from django.urls import path, include
from . import views

urlpatterns = [
  path('solicitante',views.solicitante, name='solicitante'),
  path('tiposolicitante',views.tipoSolicitante, name='tiposolicitante'),
  path('tractorista',views.tractoristas, name='tractorista'),
]
