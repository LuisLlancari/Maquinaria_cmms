from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from .viewss import componentes
from .viewss import sistema
urlpatterns = [
  path('', componentes.componente, name="componente"),
  path('sistema/', sistema.sistema, name="sistema"),


  path('registrar', componentes.registrarComponente, name="componente_registro"),
  path('eliminar/<int:id_componente>', componentes.eliminarComponente, name="eliminar_componente"),
  path('obtener/<int:id_componente>', componentes.obtenerDatos, name="obtener_componente"),
  path('modificar/<int:id_componente>', componentes.editarComponente, name="modificar_componente"),


  path('sistema/registrar', sistema.registrarSistema, name="sistema_registro"),
  path('sistema/eliminar/<int:id_sistema>', sistema.eliminarSistema, name="eliminar_sistema"),
  path('sistema/obtener/<int:id_sistema>', sistema.obtenerDatos, name="obtener_sistema"),
  path('sistema/modificar/<int:id_sistema>', sistema.editarSistema, name="modificar_sistema"),



  
]
