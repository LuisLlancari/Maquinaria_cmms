# Generated by Django 5.0.3 on 2024-04-11 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ceco', '0001_initial'),
        ('componente_pieza', '0001_initial'),
        ('localizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('idresponsable', models.AutoField(primary_key=True, serialize=False)),
                ('responsable', models.CharField(blank=True, max_length=40, null=True, verbose_name='Responsable')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
                'ordering': ['responsable'],
            },
        ),
        migrations.CreateModel(
            name='TipoImplemento',
            fields=[
                ('idtipoimplemento', models.AutoField(primary_key=True, serialize=False)),
                ('tipoimplemento', models.CharField(max_length=45, unique=True, verbose_name='Tipo Implemento')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tipo Implemento',
                'verbose_name_plural': 'Tipos de Implementos',
                'ordering': ['tipoimplemento'],
            },
        ),
        migrations.CreateModel(
            name='Implemento',
            fields=[
                ('idimplemento', models.AutoField(primary_key=True, serialize=False)),
                ('implemento', models.CharField(max_length=45, verbose_name='Implemento')),
                ('tiempovida', models.IntegerField(verbose_name='Tiempo de vida')),
                ('nroimplemento', models.CharField(max_length=12, verbose_name='Numero de Implemento')),
                ('codimplemento', models.CharField(max_length=12, verbose_name='Codigo de Implemento')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
                ('idarea', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='localizacion.area', verbose_name='Area')),
                ('idtipoimplemento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='implemento.tipoimplemento', verbose_name='Tipo Implemento')),
            ],
            options={
                'verbose_name': 'Implemento',
                'verbose_name_plural': 'Implementos',
                'ordering': ['implemento', 'idtipoimplemento'],
            },
        ),
        migrations.CreateModel(
            name='DetImplementos',
            fields=[
                ('iddetalleimplemento', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
                ('idceco', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='ceco.ceco', verbose_name='CECO')),
                ('idpieza', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='componente_pieza.pieza', verbose_name='Pieza')),
                ('idimplemento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='implemento.implemento', verbose_name='Implemento')),
                ('idresponsable', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='implemento.responsable', verbose_name='Responsable')),
            ],
            options={
                'verbose_name': 'Detalle Implemento',
                'verbose_name_plural': 'Detalle Implementos',
                'ordering': ['idpieza', 'idresponsable', 'creado_en'],
            },
        ),
    ]
