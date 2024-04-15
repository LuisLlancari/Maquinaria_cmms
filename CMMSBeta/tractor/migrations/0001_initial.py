# Generated by Django 4.2.10 on 2024-04-15 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteTractor',
            fields=[
                ('idreportetractor', models.AutoField(primary_key=True, serialize=False)),
                ('horometroinicial', models.IntegerField(verbose_name='Horómetro Inicial')),
                ('horometrofinal', models.IntegerField(verbose_name='Horómetro Final')),
                ('correlativo', models.IntegerField(verbose_name='Correlativo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Reporte Tractor',
                'verbose_name_plural': 'Reportes Tractores',
            },
        ),
        migrations.CreateModel(
            name='TipoTractor',
            fields=[
                ('idtipotractor', models.AutoField(primary_key=True, serialize=False)),
                ('tipotractor', models.CharField(max_length=50, verbose_name='Tipo Tractor')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tipo Tractor',
                'verbose_name_plural': 'Tipos Tractores',
            },
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('idtractor', models.AutoField(primary_key=True, serialize=False)),
                ('nrotractor', models.IntegerField(verbose_name='Número Tractor')),
                ('horainicial', models.IntegerField(verbose_name='Hora Inicial')),
                ('horauso', models.IntegerField(verbose_name='Hora Uso')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idtipotractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tractor.tipotractor', verbose_name='Tipo Tractor')),
            ],
            options={
                'verbose_name': 'Tractor',
                'verbose_name_plural': 'Tractores',
            },
        ),
    ]
