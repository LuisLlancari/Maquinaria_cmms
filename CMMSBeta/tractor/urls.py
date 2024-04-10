from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reportetractor, name='reportetractor'),
    path('tipotractor', views.tipotractor, name='tipotractor'),
    path('tractor', views.tractor, name='tractor'),
]