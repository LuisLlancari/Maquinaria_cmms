from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from . import views

urlpatterns = [
  path('', views.componente, name="componente"),
  path('pieza', views.pieza, name="pieza"),
  path('sistema', views.sistema, name="sistema"),
  path('sistema/registrar', views.registrarSistema, name="sistema_registro"),
  path('sistema/eliminar/<int:id_sistema>', views.eliminarSistema, name="eliminar_sistema"),
]
