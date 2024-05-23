from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from .viewss import componentes
from .viewss import sistema
from .viewss import piezas
from .viewss import configuracion
from .viewss import det_conponente
from .viewss import detalle_cong

urlpatterns = [
  path('', componentes.componente, name="componente"),
  path('sistema/', sistema.sistema, name="sistema"),
  path('pieza/', piezas.piezas, name="pieza"),
  path('det_componente/', det_conponente.det_componente, name="det_componente"),


  path('registrar', componentes.registrarComponente, name="componente_registro"),
  path('eliminar/<int:id_componente>', componentes.eliminarComponente, name="eliminar_componente"),
  path('obtener/<int:id_componente>', componentes.obtenerDatos, name="obtener_componente"),
  path('modificar/<int:id_componente>', componentes.editarComponente, name="modificar_componente"),


  path('sistema/registrar', sistema.registrarSistema, name="sistema_registro"),
  path('sistema/eliminar/<int:id_sistema>', sistema.eliminarSistema, name="eliminar_sistema"),
  path('sistema/obtener/<int:id_sistema>', sistema.obtenerDatos, name="obtener_sistema"),
  path('sistema/modificar/<int:id_sistema>', sistema.editarSistema, name="modificar_sistema"),

  path('pieza/registrar', piezas.registrarPieza, name="pieza_registro"),
  path('pieza/eliminar/<int:id_pieza>', piezas.eliminarPieza, name="eliminar_pieza"),
  path('pieza/obtener/<int:id_pieza>', piezas.obtenerDatos, name="obtener_pieza"),
  path('pieza/modificar/<int:id_pieza>', piezas.editarPieza, name="modificar_pieza"),

  path('det_componente/registrar', det_conponente.registrarDetalleComponente, name="det_componente_registro"),

  path('configuracion/', configuracion.configuracion, name="configuracion"),
  path('detalle_cong/', detalle_cong.detalle_cong, name="detalle_cong"),



  
]
