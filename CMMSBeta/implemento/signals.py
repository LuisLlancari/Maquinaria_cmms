from django.db.models.signals import post_save, pre_save
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models import F
from .models import Implemento, DetImplementos, ImplementoSupervisor
from mantenimiento.models import Mantenimiento, ProgramacionMantenimiento 
from componente_pieza.models import DetalleComponente, DetalleConfiguracion, Componente, Pieza

@receiver(post_save, sender = Implemento)
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
            # Instancioamos implemento en una variable
            inst_implemento = Implemento.objects.get(idimplemento=id_implemento)


            # Obtener los componentes relacionados con la configuración
            det_comp = DetalleConfiguracion.objects.filter(idconfiguracion=id_configuracion).values('idcomponente')

            for componente in det_comp:
                id_componente = componente['idcomponente']

                # Obtener las piezas relacionadas con el componente
                det_componentes = DetalleComponente.objects.filter(idcomponente=id_componente).values(
                'iddetallecomponente','idcomponente','idpieza', 'cantidad')

                for det_componente in det_componentes:
                    id_detcomponente = det_componente['iddetallecomponente']
                    cant_pieza = det_componente['cantidad']
                    inst_detcomponente = get_object_or_404(DetalleComponente,iddetallecomponente =id_detcomponente)

                    #   Crear el detalle del implemento
                    DetImplementos.objects.create(
                    idimplemento=inst_implemento, 
                    iddetallecomponente = inst_detcomponente,
                    HUcomponente=horauso_implemento,
                    HUpieza=horauso_implemento,
                    cantidadpieza=cant_pieza)

def creacion_programacion(FM, HU, proximo_mantenimiento, id_implemento):
    if FM is None or HU is None:
        return 0, 0
    
    horas_antes = proximo_mantenimiento - 50

    # Obtenemos el implemento ligado al usuario
    implemento = get_object_or_404(ImplementoSupervisor, estado=True, idimplemento = id_implemento)

    if HU >= horas_antes:
        ProgramacionMantenimiento.objects.create(idimplemento = implemento, tipomantenimiento = 1)
        pass


@receiver(pre_save, sender=Implemento)
def verificar_horasdeuso(sender, instance, **kwargs):
   if instance.pk:
    old_instance = Implemento.objects.get(pk = instance.pk)
    if old_instance.horasdeuso != instance.horasdeuso:  
        print("El implemento tiene un modicacion de horauso")


        id_implemento = instance.pk

        implemento_sup = get_object_or_404(ImplementoSupervisor, idimplemento = id_implemento, estado = True)
        id_implementosup = implemento_sup.idimplementosupervisor

        hora_uso = instance.horasdeuso
        frecuencia_mantenimiento = instance.idtipoimplemento.frecuencia_man
        proximo_mantenimiento = instance.proximo_mantenimiento


        if not ProgramacionMantenimiento.objects.filter(idimplemento = id_implementosup , estado = True).exists():
            print('no existe ninguna programacion con este implemento')
            creacion_programacion(frecuencia_mantenimiento, hora_uso, proximo_mantenimiento, id_implemento)
        else:
            print('El implemento tiene una programacion activa')

# Crea el proximo mantenimiento cuando un implemento es creado
@receiver(pre_save, sender=Implemento)
def set_proximo_mantenimiento(sender, instance, **kwargs):
    if instance._state.adding and instance.idtipoimplemento and instance.horasdeuso is not None:
        frecuencia_mantenimiento = instance.idtipoimplemento.frecuencia_man
        if frecuencia_mantenimiento > 0:
            if instance.horasdeuso < frecuencia_mantenimiento:
                instance.proximo_mantenimiento = frecuencia_mantenimiento
            else:
                instance.proximo_mantenimiento = ((instance.horasdeuso // frecuencia_mantenimiento) + 1) * frecuencia_mantenimiento