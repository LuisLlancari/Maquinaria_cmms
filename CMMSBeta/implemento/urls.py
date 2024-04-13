from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from .viewss import detalle, implemento, tipos 

urlpatterns = [
  path('', implemento.implemento , name='implemento'),
  path('tipos', tipos.tipoImplemento , name='tipoimplemento'),
  path('detalle', detalle.detalleImplemento   , name='detalleimplemento'),

  path('tipos/registrar', tipos.registrarTipoImplemento, name="registrar_tipo"),
  path('tipos/eliminar/<int:id>', tipos.eliminarImplemento, name="eliminar_tipo"),
  path('tipos/obtener/<int:id_tipo>', tipos.obtenerDatos, name="obtener_tipo"),
  path('tipos/modificar/<int:id_tipo>', tipos.editarTipoImplemento, name="modificar_tipo"),


  path('implemento/registrar', implemento.registrarImplemento, name="registrar_implemento"),
  path('implemento/eliminar/<int:id_implemento>', implemento.eliminarimplemento, name="eliminar_implemento"),
  path('obtener/<int:id_implemento>', implemento.obtenerDatos, name="obtener_implemento"),
  path('modificar/<int:id_implemento>', implemento.editarImplemento, name="modificar_implemento"),

  path('detalle/registrar', detalle.registrarDetalle, name="registrar_detalle"),
  path('detalle/eliminar/<int:id_detalle>', detalle.eliminarDetalle, name="eliminar_detalle"),
  path('detalle/obtener/<int:id_detimplemento>', detalle.obtenerDatos, name="obtener_detalle"),
  path('detalle/modificar/<int:id_detimplemento>', detalle.editarDetalle, name="modificar_detalle"),


]
