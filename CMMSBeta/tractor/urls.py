from django.urls import path, include
from .views import tipotractor, tractor, reportetractor

urlpatterns = [
    path('', reportetractor.reportetractor, name='reportetractor'),
    path('tipotractor', tipotractor.tipotractor, name='tipotractor'),
    path('tractor/', tractor.tractor, name='tractor'),

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
]