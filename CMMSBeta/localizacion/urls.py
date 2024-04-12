from django.urls import path, include
from .views import views, sede

urlpatterns = [
    path('', views.area, name='area'),
    path('base', views.base, name='base'),
     path('sede', sede.sede , name='sede'),
]