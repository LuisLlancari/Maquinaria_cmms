from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from mantenimiento.models import ProgramacionMantenimiento, Mantenimiento

@receiver(post_save, sender = ProgramacionMantenimiento)
def creacion_mantenimiento(sender, instance, **kwargs):
  if instance.pk and instance.fechaprogramacion:
    idprogramacion = instance.idprogramacionmantenimiento
    if Mantenimiento.objects.filter(idprogramacionmantenimiento = idprogramacion, estado= 1).exists():
      pass
    else:
      Mantenimiento.objects.create(
        idprogramacionmantenimiento_id = idprogramacion
      )
