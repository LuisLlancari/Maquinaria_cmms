from django.urls import path, include
from .view import roles, usuarios


urlpatterns = [
  
   path('registro_usuario', usuarios.gestorUsuario, name="registro_usuario"),
   path('registro_usuario/registrar', usuarios.registrarUsuario, name="registrar_usuario"),

   
   #Rol
   path('roles', roles.roles, name="roles"),
   path('eliminar_rol/<int:idrol>', roles.eliminar_rol, name="eliminar_rol"),
   path('registrar_rol', roles.registrar_rol, name="registrar_rol"),
   path('editar_rol', roles.editar_rol, name="editar_rol"),
]
