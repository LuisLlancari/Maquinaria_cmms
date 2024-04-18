# Generated by Django 4.2.10 on 2024-04-18 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operarios', '0003_delete_reportetractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitante',
            name='estado_actividad',
            field=models.BooleanField(default=True, verbose_name='Estado Actividad'),
        ),
        migrations.AddField(
            model_name='tractorista',
            name='estado_actividad',
            field=models.BooleanField(default=True, verbose_name='Estado Actividad'),
        ),
        migrations.AddField(
            model_name='tractorista',
            name='idusuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
