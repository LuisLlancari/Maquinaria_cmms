from django.urls import path, include
from .views import solicitante, tipos_solicitante, tractorista, encargado

urlpatterns = [
  path('solicitante',solicitante.solicitante, name='solicitante'),
  path('tiposolicitante',tipos_solicitante.tipoSolicitante, name='tiposolicitante'),
  path('tractorista',tractorista.tractoristas, name='tractorista'),

  path('tiposolicitante/registrar', tipos_solicitante.registrartipoSolicitante, name="tiposolicitante_registro"),
  path('tiposolicitante/eliminar/<int:id_tipo>', tipos_solicitante.eliminarTiposolicitante, name="tiposolicitante_eliminar"),
  path('tiposolicitante/obtener/<int:id_tipo>', tipos_solicitante.obtenerDatos, name="obtener_tiposolicitante"),
  path('tiposolicitante/modificar/<int:id_tipo>', tipos_solicitante.editarTiposolicitante, name="modificar_tiposolicitante"),


  path('solicitante/registrar', solicitante.registrarSolicitante, name="solicitante_registro"),
  path('solicitante/eliminar/<int:id_solicitante>', solicitante.eliminarSolicitante, name="solicitante_eliminar"),
  path('solicitante/obtener/<int:id_solicitante>', solicitante.obtenerDatos, name="obtener_solicitante"),
  path('solicitante/modificar/<int:id_solicitante>', solicitante.editarSolicitante, name="modificar_solicitante"),


  path('tractorista/registrar', tractorista.registrarTractorista, name="tractorista_registro"),
  path('tractorista/eliminar/<int:id_tractorista>', tractorista.eliminarTractorista, name="tractorista_eliminar"),
  path('tractorista/obtener/<int:id_tractorista>', tractorista.obtenerDatos, name="obtener_tractorista"),
  path('tractorista/modificar/<int:id_tractorista>', tractorista.editarTractoristas, name="modificar_tractorista"),

  path('encargado', encargado.responsable, name='responsable'),
  path('encargado/registrar_responsable',encargado.registrar_responsable, name='registrar_responsable'),
  path('encargado/editar_responsable/<int:id_encargado>',encargado.editar_responsable, name='editar_responsable'),
  path('encargado/eliminar_responsable/<int:id_encargado>', encargado.eliminar_responsable, name='eliminar_responsable'),
  path('encargado/obtener/<int:id_encargado>', encargado.obtenerDatos, name='obtener_encargado'),

]
