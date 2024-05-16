# Generated by Django 4.2.10 on 2024-05-14 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programacion_labor', '0001_initial'),
        ('operarios', '0001_initial'),
        ('tractor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='idtractor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tractor.tractor', verbose_name='Tractor'),
        ),
        migrations.AddField(
            model_name='programacion',
            name='idtractorista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operarios.tractorista', verbose_name='Tractorista'),
        ),
    ]
