# Generated by Django 4.2.10 on 2024-04-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componente_pieza', '0002_alter_componente_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='componente',
            name='frecuencia_man',
            field=models.IntegerField(blank=True, null=True, verbose_name='Frecuencia de mantenimiento'),
        ),
    ]
