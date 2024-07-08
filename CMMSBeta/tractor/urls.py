from django.urls import path, include
from .views import tipotractor, tractor, reportetractor, tractorsupervisor as trcsup

urlpatterns = [
    path('', tractor.tractor, name='tractor'),
    path('tipotractor', tipotractor.tipotractor, name='tipotractor'),
    path('reportetractor/', reportetractor.reportetractor, name='reportetractor'),

    # funciones reporte
    path('reportetractor/registrar', reportetractor.registrarReporte, name='registrar_reporte' ),
    path('reportetractor/obtenerhinicial/<int:id_tractor>', reportetractor.obtenerHorainicial, name='obtener_horaini' ),
    
    #funciones tipotractor
    path('eliminar_tipotractor/<int:idtractor>', tipotractor.eliminar_tipotractor, name='eliminar_tipotractor'), 
    path('registrar_tipotractor', tipotractor.registrar_tipotractor, name='registrar_tipotractor'), 
    path('editar_tipo', tipotractor.editar_tipo, name='editar_tipo'), 
    
    #funciones tractores
    path('eliminartractor/<int:idtractor>', tractor.eliminar_tractor, name='eliminartractor'), 
    path('registrar_tractor', tractor.registrar_tractor, name='registrar_tractor'), 
    path('editar_tractor', tractor.editar_tractor, name='editar_tractor'),
    path('asignar_supervisor/<int:id_tractor>', tractor.AsignarSupervisor, name="tractor_asignar_supervisor"),
    path('quitar_supervisor/<int:id_tractor>', tractor.QuitarSupervisor, name="tractor_quitar_supervisor"),
  

    path('asignar_supervisor', trcsup.tractorSupervisor, name="asignar_supervisor_tractor" ),
    path('asignar_supervisor/registrar', trcsup.registrartractorSupervisor, name="asignar_supervisor_tractor_registrar" ),
    path('asignar_supervisor/eliminar/<int:id_registro>', trcsup.eliminartractorSupervisor, name="asignar_supervisor_tractor_eliminar" ),
    path('asignar_supervisor/fechasalida/<int:id_registro>', trcsup.registrarFechaSalidaSupervisor, name="asignar_supervisor_tractor_fecha_salida" ),

]