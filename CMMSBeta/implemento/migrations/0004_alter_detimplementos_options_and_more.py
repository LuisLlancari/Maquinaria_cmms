# Generated by Django 4.2.10 on 2024-04-25 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('implemento', '0003_detimplementos_sistema'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detimplementos',
            options={'verbose_name': 'Detalle Implemento', 'verbose_name_plural': 'Detalle Implementos'},
        ),
        migrations.RemoveField(
            model_name='detimplementos',
            name='idpieza',
        ),
    ]
