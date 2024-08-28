from django.urls import path, include
# Importará las vistas de la app donde te encuentres
from .views import detalle, implemento, tipos, implementosupervisor as impsup

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
  path('asignar_supervisor/<int:id_implemento>', implemento.AsignarSupervisor, name="implemento_asignar_supervisor"),
  path('quitar_supervisor/<int:id_implemento>', implemento.QuitarSupervisor, name="implemento_quitar_supervisor"),

  path('detalle/registrar', detalle.registrarDetalle, name="registrar_detalle"),
  path('detalle/eliminar/<int:id_detalle>', detalle.eliminarDetalle, name="eliminar_detalle"),
  path('detalle/obtener/<int:id_detimplemento>', detalle.obtenerDatos, name="obtener_detalle"),
  path('detalle/modificar/<int:id_detimplemento>', detalle.editarDetalle, name="modificar_detalle"),


  path('asignar_supervisor', impsup.implementoSupervisor, name="asignar_supervisor_implemento" ),
  path('asignar_supervisor/registrar', impsup.registrarImplementoSupervisor, name="asignar_supervisor_registrar" ),
  path('asignar_supervisor/eliminar/<int:id_registro>', impsup.eliminarImplementoSupervisor, name="asignar_supervisor_eliminar" ),
  path('asignar_supervisor/fechasalida/<int:id_registro>', impsup.registrarFechaSalidaSupervisor, name="asignar_supervisor_fecha_salida" ),
] 
