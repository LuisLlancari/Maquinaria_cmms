from django.urls import path, include
from .views import tipotractor

urlpatterns = [
    #path('', reportetractor.reportetractor, name='reportetractor'),
    path('', tipotractor.tipotractor, name='tipotractor'),
    #path('tractor', tractor.tractor, name='tractor'),
    
    #funciones tipotractor
    path('eliminar_tipotractor/<int:idtractor>', tipotractor.eliminar_tipotractor, name='eliminar_tipotractor'), 
    path('registrar_tipotractor', tipotractor.registrar_tipotractor, name='registrar_tipotractor'), 
    path('editar_tipo', tipotractor.editar_tipo, name='editar_tipo'), 
    
]