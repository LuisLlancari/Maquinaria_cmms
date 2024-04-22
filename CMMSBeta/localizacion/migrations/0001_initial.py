# Generated by Django 4.2.10 on 2024-04-22 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('idsede', models.AutoField(primary_key=True, serialize=False)),
                ('sede', models.CharField(max_length=50, verbose_name='Sede')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('idbase', models.AutoField(primary_key=True, serialize=False)),
                ('base', models.CharField(max_length=50, verbose_name='Base')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idsede', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacion.sede', verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Base',
                'verbose_name_plural': 'Bases',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('idarea', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=50, verbose_name='Area')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idbase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacion.base')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Area',
            },
        ),
    ]
