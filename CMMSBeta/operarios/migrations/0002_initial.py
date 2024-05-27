# Generated by Django 4.2.10 on 2024-05-25 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0001_initial'),
        ('operarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tractorista',
            name='idpersona',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='usuario.persona', verbose_name='Persona'),
        ),
        migrations.AddField(
            model_name='tractorista',
            name='idusuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='solicitante',
            name='idpersona',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='usuario.persona', verbose_name='Persona'),
        ),
        migrations.AddField(
            model_name='solicitante',
            name='idtiposolicitante',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='operarios.tiposolicitante', verbose_name='Tipo Solicitante'),
        ),
    ]
