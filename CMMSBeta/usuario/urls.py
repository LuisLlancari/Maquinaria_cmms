from django.urls import path, include
from .view import roles


urlpatterns = [
   # path('login', views.login_user, name="login"),
   # path('logout', views.logout_user, name="logout"),
   
   #Rol
   path('roles', roles.roles, name="roles"),
   path('eliminar_rol/<int:idrol>', roles.eliminar_rol, name="eliminar_rol"),
   path('registrar_rol', roles.registrar_rol, name="registrar_rol"),
   path('editar_rol', roles.editar_rol, name="editar_rol"),
]
