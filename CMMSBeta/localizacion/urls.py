from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.area, name='area'),
    path('base', views.base, name='base'),
    path('sede', views.sede, name='sede'),
    path('registrar_sede', views.registrar_sede, name='registrar_sede'),
    path('editar_sede/<int:sede_id>/', views.editar_sede, name='editar_sede'),
    path('eliminar_sede/<int:sede_id>/', views.eliminar_sede, name='eliminar_sede'),
]