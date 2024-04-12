from django.urls import path, include
from .views import views, sede

urlpatterns = [
    path('', views.area, name='area'),
    path('base', views.base, name='base'),
    path('sede', sede.sede , name='sede'),
    path('eliminar_sede/<int:idsede>', sede.eliminar_sede, name='eliminar_sede'), 
    path('registrar_sede', sede.registrar_sede, name='registrar_sede'), 
    path('editar_sede/<int:idsede>', sede.editar_sede, name='editar_sede'), 
]