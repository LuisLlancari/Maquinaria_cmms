from django.urls import path, include
from .views import tipotractor, tractor, reportetractor

urlpatterns = [
    path('', reportetractor.reportetractor, name='reportetractor'),
    path('tipotractor', tipotractor.tipotractor, name='tipotractor'),
    path('tractor/', tractor.tractor, name='tractor'),
    
    #funciones tipotractor
    path('eliminar_tipotractor/<int:idtractor>', tipotractor.eliminar_tipotractor, name='eliminar_tipotractor'), 
    path('registrar_tipotractor', tipotractor.registrar_tipotractor, name='registrar_tipotractor'), 
    path('editar_tipo', tipotractor.editar_tipo, name='editar_tipo'), 
    
    #funciones tractores
    path('eliminartractor/<int:idtractor>', tractor.eliminar_tractor, name='eliminartractor'), 
    path('registrar_tractor', tractor.registrar_tractor, name='registrar_tractor'), 
    
    #funciones reporte tractores
    path('eliminar_reporte/<int:idreporte>', reportetractor.eliminar_reporte, name='eliminar_reporte'), 
    path('registrar_reporte', reportetractor.registrar_reporte, name='registrar_reporte'), 
    path('editar_reporte', reportetractor.editar_reporte, name='editar_reporte'), 
    
    
    
    
]