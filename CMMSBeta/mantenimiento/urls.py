from django.urls import path, include
from .views import programacion, mantenimiento

urlpatterns = [
  path('programacion', programacion.programacion_mantenimiento, name= "programacion_mantenimiento" ),
  path('programacion/registrar_fecha/<int:id_implemento>', programacion.registrar_fecha, name= "registrar_fecha" ),
  path('programacion/registrar', programacion.registrar, name= "registrar" ),

  path('completar_programacion', mantenimiento.mantenimientos_realizados, name= "mantenimiento_realizados" ),
  path('completar_programacion/datos_mantenimiento', mantenimiento.datos_mantenimiento, name= "datos_matenimiento" ),
  path('completar_programacion/datos_implemento/<int:id_implemento>', mantenimiento.datos_implemento, name= "datos_implemento" ),
  path('completar_programacion/registrar_ingreso/<int:id_mantenimiento>', mantenimiento.registrar_ingreso, name= "registrar_ingreso" ),
  path('completar_programacion/finalizar_mantenimiento/<int:id_mantenimiento>', mantenimiento.finalizar_mantenimiento, name= "finalizar_mantenimiento" ),


]