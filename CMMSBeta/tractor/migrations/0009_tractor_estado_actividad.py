# Generated by Django 4.2.10 on 2024-04-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tractor', '0008_alter_tractor_nrotractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tractor',
            name='estado_actividad',
            field=models.BooleanField(default=True, verbose_name='Estado Actividad'),
        ),
    ]
