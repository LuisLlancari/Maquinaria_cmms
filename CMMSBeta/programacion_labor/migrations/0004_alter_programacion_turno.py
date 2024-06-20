# Generated by Django 4.2.10 on 2024-06-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programacion_labor', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programacion',
            name='turno',
            field=models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], max_length=1, verbose_name='Turno'),
        ),
    ]
