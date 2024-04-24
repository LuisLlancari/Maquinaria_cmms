# Generated by Django 4.2.10 on 2024-04-23 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundo_cultivo', '0002_alter_variedad_variedad'),
        ('tractor', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tractor',
            name='idcultivo',
        ),
        migrations.AddField(
            model_name='tractor',
            name='idfundo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fundo_cultivo.fundo', verbose_name='Fundo'),
        ),
    ]
