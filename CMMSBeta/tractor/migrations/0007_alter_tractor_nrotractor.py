# Generated by Django 4.2.10 on 2024-05-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tractor', '0006_alter_tractor_horauso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tractor',
            name='nrotractor',
            field=models.CharField(max_length=100, verbose_name='Nombre Tractor'),
        ),
    ]
