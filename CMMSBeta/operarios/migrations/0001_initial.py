# Generated by Django 4.2.10 on 2024-04-15 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSolicitante',
            fields=[
                ('idtiposolicitante', models.AutoField(primary_key=True, serialize=False)),
                ('tiposolicitante', models.CharField(max_length=45, unique=True, verbose_name='Tipo Solicitante')),
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
                ('apellidos', models.CharField(max_length=45, verbose_name='Apellidos')),
                ('nombres', models.CharField(max_length=45, verbose_name='Nombres')),
                ('codigo', models.CharField(max_length=12, verbose_name='Codigo')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tractorista',
                'verbose_name_plural': 'Tractoristas',
                'ordering': ['idtractorista', 'apellidos'],
            },
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('idsolicitante', models.AutoField(primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=45, verbose_name='Apellidos')),
                ('nombres', models.CharField(max_length=45, verbose_name='Nombres')),
                ('codigo', models.CharField(max_length=12, verbose_name='Codigo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idtiposolicitante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='operarios.tiposolicitante', verbose_name='Tipo Solicitante')),
            ],
            options={
                'verbose_name': 'Solicitante',
                'verbose_name_plural': 'Solicitantes',
                'ordering': ['idsolicitante', 'idtiposolicitante'],
            },
        ),
    ]
