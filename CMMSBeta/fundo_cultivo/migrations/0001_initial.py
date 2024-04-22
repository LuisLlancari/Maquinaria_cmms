# Generated by Django 4.2.10 on 2024-04-22 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('idcultivo', models.AutoField(primary_key=True, serialize=False)),
                ('cultivo', models.CharField(max_length=30, unique=True, verbose_name='Cultivo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cultivo',
                'verbose_name_plural': 'Cultivos',
            },
        ),
        migrations.CreateModel(
            name='Fundo',
            fields=[
                ('idfundo', models.AutoField(primary_key=True, serialize=False)),
                ('fundo', models.CharField(max_length=30, unique=True, verbose_name='Fundo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idsede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='localizacion.sede', verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Fundo',
                'verbose_name_plural': 'Fundos',
            },
        ),
        migrations.CreateModel(
            name='Variedad',
            fields=[
                ('idvariedad', models.AutoField(primary_key=True, serialize=False)),
                ('variedad', models.CharField(max_length=30, unique=True, verbose_name='Variedad')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idcultivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundo_cultivo.cultivo', verbose_name='Cultivo')),
            ],
            options={
                'verbose_name': 'Variedad',
                'verbose_name_plural': 'Variedades',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('idlote', models.AutoField(primary_key=True, serialize=False)),
                ('lote', models.CharField(max_length=30, unique=True, verbose_name='Lote')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idfundo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundo_cultivo.fundo', verbose_name='Fundo')),
                ('idvariedad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fundo_cultivo.variedad', verbose_name='Variedad')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
            },
        ),
    ]
