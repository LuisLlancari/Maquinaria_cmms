from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from .viewss import componentes
from .viewss import pieza
from .viewss import sistema
urlpatterns = [
  path('', componentes.componente, name="componente"),
  path('pieza/', pieza.pieza, name="pieza"),
  path('sistema/', sistema.sistema, name="sistema"),


  path('registrar', componentes.registrarComponente, name="componente_registro"),
  path('eliminar/<int:id_componente>', componentes.eliminarComponente, name="eliminar_componente"),
  path('obtener/<int:id_componente>', componentes.obtenerDatos, name="obtener_componente"),
  path('modificar/<int:id_componente>', componentes.editarComponente, name="modificar_componente"),


  path('sistema/registrar', sistema.registrarSistema, name="sistema_registro"),
  path('sistema/eliminar/<int:id_sistema>', sistema.eliminarSistema, name="eliminar_sistema"),
  path('sistema/obtener/<int:id_sistema>', sistema.obtenerDatos, name="obtener_sistema"),
  path('sistema/modificar/<int:id_sistema>', sistema.editarSistema, name="modificar_sistema"),


  path('pieza/registrar', pieza.registrarPieza, name="pieza_registro"),
  path('pieza/eliminar/<int:id_pieza>', pieza.eliminarPieza, name="eliminar_pieza"),
  path('pieza/obtener/<int:id_pieza>', pieza.obtenerDatos, name="obtener_pieza"),
  path('pieza/modificar/<int:id_pieza>', pieza.editarPieza, name="modificar_pieza"),
  

  # path('componente/eliinar', componentes.registrarComponente, name="componente_registro"),

  
]
