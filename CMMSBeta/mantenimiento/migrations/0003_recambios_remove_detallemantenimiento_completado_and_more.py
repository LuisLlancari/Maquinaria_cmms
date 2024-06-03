# Generated by Django 4.2.10 on 2024-06-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recambios',
            fields=[
                ('idrecambio', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=45, verbose_name='Parte del recambio')),
                ('codigo', models.CharField(max_length=12, verbose_name='Codigo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Recambio',
                'verbose_name_plural': 'Recambios',
            },
        ),
        migrations.RemoveField(
            model_name='detallemantenimiento',
            name='completado',
        ),
        migrations.AddField(
            model_name='detallemantenimiento',
            name='Realizado',
            field=models.BooleanField(default=True, verbose_name='Realizado'),
        ),
    ]
