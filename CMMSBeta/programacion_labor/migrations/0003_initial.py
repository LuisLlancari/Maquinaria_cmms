# Generated by Django 4.2.10 on 2024-05-25 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programacion_labor', '0002_initial'),
        ('implemento', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='idusuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='detallelabor',
            name='idimplemento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='implemento.implemento', verbose_name='Implemento'),
        ),
        migrations.AddField(
            model_name='detallelabor',
            name='idprogramacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programacion_labor.programacion', verbose_name='Programacion'),
        ),
    ]
