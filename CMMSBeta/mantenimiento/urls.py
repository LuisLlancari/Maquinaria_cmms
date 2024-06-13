from django.urls import path, include
from .views import mantenimiento_proceso, programacion, mantenimiento_inicio, mantenimientos_realizado

urlpatterns = [
  path('programacion', programacion.programacion_mantenimiento, name= "programacion_mantenimiento" ),
  path('programacion/registrar_fecha/<int:id_implemento>', programacion.registrar_fecha, name= "registrar_fecha" ),
  path('programacion/registrar', programacion.registrar, name= "registrar" ),
  path('programacion/eliminar_programacion/<int:id_programacion>', programacion.eliminar_programacion, name= "eliminar_programacion" ),
  path('programacion/editarFecha', programacion.editar_fecha, name= "editarFecha" ),
  path('programacion/datos_mantenimiento/<int:id_programacion>', programacion.datos_mantenimiento, name= "datos_matenimiento_realizado" ),

  path('pendiente', mantenimiento_inicio.mantenimiento_pendiente, name= "mantenimiento_pendiente" ),
  path('pendiente/datos_mantenimiento', mantenimiento_inicio.datos_mantenimiento, name= "datos_mantenimiento_pendientes" ),
  path('pendiente/registrar_ingreso/<int:id_mantenimiento>', mantenimiento_inicio.registrar_ingreso, name= "registrar_ingreso" ),

  path('proceso', mantenimiento_proceso.mantenimiento_proceso, name= "mantenimiento_proceso" ),
  path('proceso/datos_mantenimiento', mantenimiento_proceso.datos_mantenimiento, name= "datos_matenimiento_proceso" ),
  path('proceso/datos_implemento/<int:id_programacion>/<int:id_implemento>', mantenimiento_proceso.datos_implemento, name= "datos_implemento" ),
  path('proceso/finalizar_mantenimiento/<int:id_mantenimiento>', mantenimiento_proceso.finalizar_mantenimiento, name= "finalizar_mantenimiento" ),

  path('realizados', mantenimientos_realizado.mantenimientos_realizados, name= "mantenimientos_realizados" ),
  path('realizados/datos_mantenimiento', mantenimientos_realizado.datos_mantenimientos, name= "datos_matenimiento_realizado" ),
  path('realizado/detalle_mantenimiento/<int:id_mantenimiento>', mantenimientos_realizado.detalle_mantenimiento, name= "obtener_detallemantenimiento" ),



]