from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import F
from .models import Implemento, DetImplementos
from mantenimiento.models import Mantenimiento, ProgramacionMantenimiento 
from componente_pieza.models import DetalleComponente, DettaleConfiguracion, Componente, Pieza

@receiver(post_save, sender =Implemento)
def creacionDetalleImplemento(sender, instance, created, **kwargs):
  if created:
      # Obtener la configuración del implemento recién creado
      det_config = Implemento.objects.filter(idimplemento=instance.idimplemento).annotate(
          idconfiguracion=F('idtipoimplemento__idconfiguracion_implemento__idconfiguraciontipoimplemento'),
      ).values('idconfiguracion', 'horasdeuso', 'idimplemento')

      if det_config.exists():
        # Asignamos valores del det_config a variables
        config = det_config[0]
        id_implemento = config['idimplemento']
        horauso_implemento = config['horasdeuso']
        id_configuracion = config['idconfiguracion']

        # Obtener los componentes relacionados con la configuración
        det_comp = DettaleConfiguracion.objects.filter(idconfiguracion=id_configuracion).values('idcomponente')

        for componente in det_comp:
            id_componente = componente['idcomponente']

            # Obtener las piezas relacionadas con el componente
            det_pieza = DetalleComponente.objects.filter(idcomponente=id_componente).values('idpieza', 'cantidad')

            for pieza in det_pieza:
                id_pieza = pieza['idpieza']
                cant_pieza = pieza['cantidad']

                # Crear instancias de los modelos relacionados
                inst_implemento = Implemento.objects.get(idimplemento=id_implemento)
                inst_componente = Componente.objects.get(idcomponente=id_componente)
                inst_pieza = Pieza.objects.get(idpieza=id_pieza)

                # Crear el detalle del implemento
                DetImplementos.objects.create(
                    idimplemento=inst_implemento, 
                    idcomponente=inst_componente,
                    HUcomponente=horauso_implemento,
                    idpieza=inst_pieza,
                    HUpieza=horauso_implemento,
                    cantidadpieza=cant_pieza)


def creacion_programacion(FM, HU, id_implemento):
    if FM is None or HU is None:
        return 0, 0
    if HU < FM:
        FM -= 50
        if HU >= FM:
            ProgramacionMantenimiento.objects.create(idimplemento_id = id_implemento)
    else:
        FM -= 50
        residuo_horauso = HU % FM
        if residuo_horauso >= FM:
            ProgramacionMantenimiento.objects.create(idimplemento_id = id_implemento)


@receiver(pre_save, sender=Implemento)
def implemento_post_save(sender, instance, **kwargs):
   if instance.pk:
    old_instance = Implemento.objects.get(pk = instance.pk)
    if old_instance.horasdeuso != instance.horasdeuso:  

        id_implemento = instance.pk
        hora_uso = instance.horasdeuso
        frecuencia_mantenimiento = instance.idtipoimplemento.frecuencia_man
        if ProgramacionMantenimiento.objects.filter(idimplemento = id_implemento , estado = 1).exists():
           pass
        else:
            creacion_programacion(frecuencia_mantenimiento, hora_uso, id_implemento)

