from django.urls import path, include
from .view import roles, usuarios


urlpatterns = [
   # del gestor usuario
   path('registro_usuario', usuarios.gestorUsuario, name="registro_usuario"),
   path('registro_usuario/registrar', usuarios.registrarUsuario, name="registrar_usuario"),
   path('obtener_usuario/<int:id_usuario>', usuarios.obtenerUsuario, name="obtener_usuario"),
   path('restablecer_clave/<int:id_usuario>', usuarios.restablecerContraseña, name="restablecer_clave"),
   path('modificar_usuario/<int:id_usuario>', usuarios.editarUsuario, name="modificar_usuario"),
   path('eliminar_usuario/<int:id_usuario>', usuarios.eliminarUsuario, name="eliminar_usuario"),

   
   # Roles
   path('roles', roles.roles, name="roles"),
   path('eliminar_rol/<int:idrol>', roles.eliminar_rol, name="eliminar_rol"),
   path('registrar_rol', roles.registrar_rol, name="registrar_rol"),
   path('editar_rol', roles.editar_rol, name="editar_rol"),
]
