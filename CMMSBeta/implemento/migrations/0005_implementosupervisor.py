# Generated by Django 4.2.10 on 2024-06-28 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('implemento', '0004_implemento_proximo_mantenimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImplementoSupervisor',
            fields=[
                ('idimplementosupervisor', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('fechaInicio', models.DateField(auto_now=True, verbose_name='Fecha Inicio')),
                ('fechaFin', models.DateField(verbose_name='Fecha Fin')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idimplemento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='implemento.implemento', verbose_name='Implemento')),
                ('idsupervisor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Implemento por supervisor',
                'verbose_name_plural': 'Implementos por supervisores',
            },
        ),
    ]
