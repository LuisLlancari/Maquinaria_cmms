from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.area, name='area'),
    path('base', views.base, name='base'),
    path('sede', views.sede, name='sede'),
]