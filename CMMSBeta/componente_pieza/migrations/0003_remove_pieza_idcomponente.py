# Generated by Django 4.2.10 on 2024-05-21 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('componente_pieza', '0002_detallecomponente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pieza',
            name='idcomponente',
        ),
    ]
