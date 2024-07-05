from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from .views import componentes
from .views import sistema
from .views import piezas
from .views import configuracion
from .views import det_conponente
from .views import detalle_cong

urlpatterns = [
  path('', componentes.componente, name="componente"),
  path('sistema/', sistema.sistema, name="sistema"),
  path('pieza/', piezas.piezas, name="pieza"),
  path('det_componente/', det_conponente.det_componente, name="det_componente"),
  path('configuracion/', configuracion.configuracion, name="configuracion"),
  path('detalle_cong/', detalle_cong.detalle_cong, name="detalle_cong"),


  path('registrar', componentes.registrarComponente, name="componente_registro"),
  path('eliminar/<int:id_componente>', componentes.eliminarComponente, name="eliminar_componente"),
  path('obtener/<int:id_componente>', componentes.obtenerDatos, name="obtener_componente"),
  path('obtener_piezas/<int:id_componente>', componentes.obtenerPiezas, name="obtener_piezas"),
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
  path('configuracion/registrar', configuracion.registrarConfiguracion, name="registrar_configuracion"),
  path('configuracion/obtener/<int:id_configuracion>', configuracion.obtener, name="obtener"),
  path('configuracion/eliminar/<int:id_configuracion>', configuracion.eliminarConfiguracion, name="eliminar_configuracion"),

  path('detalle_cong/registrar', detalle_cong.registrarDetalleConfiguracion, name="detalle_cong_registro"),



  
]
