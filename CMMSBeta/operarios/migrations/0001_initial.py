# Generated by Django 4.2.10 on 2024-06-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('idsolicitante', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('estado_actividad', models.BooleanField(default=True, verbose_name='Estado Actividad')),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, null=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Solicitante',
                'verbose_name_plural': 'Solicitantes',
                'ordering': ['idsolicitante', 'idtiposolicitante'],
            },
        ),
        migrations.CreateModel(
            name='TipoSolicitante',
            fields=[
                ('idtiposolicitante', models.AutoField(primary_key=True, serialize=False)),
                ('tiposolicitante', models.CharField(max_length=45, verbose_name='Tipo Solicitante')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tipo Solicitante',
                'verbose_name_plural': 'Tipos de Solicitantes',
                'ordering': ['tiposolicitante'],
            },
        ),
        migrations.CreateModel(
            name='Tractorista',
            fields=[
                ('idtractorista', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('estado_actividad', models.BooleanField(default=True, verbose_name='Estado Actividad')),
                ('creado_en', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Tractorista',
                'verbose_name_plural': 'Tractoristas',
                'ordering': ['idtractorista'],
            },
        ),
    ]
