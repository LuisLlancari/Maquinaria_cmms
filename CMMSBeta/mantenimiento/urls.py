from django.urls import path, include
from .views import programacion, mantenimiento

urlpatterns = [
  path('programacion', programacion.programacion_mantenimiento, name= "programacion_mantenimiento" ),
  path('programacion/registrar_fecha/<int:id_implemento>', programacion.registrar_fecha, name= "registrar_fecha" ),

  path('completar_programacion', mantenimiento.mantenimientos_realizados, name= "mantenimiento_realizados" ),
  path('completar_programacion/datos_mantenimiento', mantenimiento.datos_mantenimiento, name= "datos_matenimiento" ),
  path('completar_programacion/registrar_ingreso/<int:id_mantenimiento>', mantenimiento.registrar_ingreso, name= "registrar_ingreso" ),

]