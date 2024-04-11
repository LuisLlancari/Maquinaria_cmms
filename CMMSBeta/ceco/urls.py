from django.urls import path
from . import views

urlpatterns = [
    #Urls de ceco
    path('', views.ceco, name='ceco'),
    path('registrar_ceco', views.registrar_ceco, name='registrar_ceco'),
    path('editar_ceco', views.editar_ceco, name='editar_ceco'),


    #Urls de responsable
    path('responsable', views.responsable, name='responsable'),
]