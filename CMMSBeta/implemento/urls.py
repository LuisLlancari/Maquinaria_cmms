from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from . import views

urlpatterns = [
  path('implemento', views.implento , name='implemento')
]
