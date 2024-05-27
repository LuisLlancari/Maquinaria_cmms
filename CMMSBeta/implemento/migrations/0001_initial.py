# Generated by Django 4.2.10 on 2024-05-25 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ceco', '0001_initial'),
        ('componente_pieza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetImplementos',
            fields=[
                ('iddetalleimplemento', models.AutoField(primary_key=True, serialize=False)),
                ('MRimplemento', models.IntegerField(default=0, verbose_name='Mantenimientos realizados al implemento')),
                ('MRcomponente', models.IntegerField(default=0, verbose_name='Mantenimientos realizados al componente')),
                ('HUcomponente', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Horas de uso del componente')),
                ('CRcomponente', models.IntegerField(default=0, verbose_name='Cambios realizados al componente')),
                ('cantidadpieza', models.IntegerField(default=0, verbose_name='Cantidad de piezas')),
                ('MRpieza', models.IntegerField(default=0, verbose_name='Mantenimientos realizados a la pieza')),
                ('HUpieza', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Horas de uso de la pieza')),
                ('CRpieza', models.IntegerField(default=0, verbose_name='Cambios realizados a la pieza')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Detalle Implemento',
                'verbose_name_plural': 'Detalle Implementos',
            },
        ),
        migrations.CreateModel(
            name='TipoImplemento',
            fields=[
                ('idtipoimplemento', models.AutoField(primary_key=True, serialize=False)),
                ('tipoimplemento', models.CharField(max_length=45, verbose_name='Tipo Implemento')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('tiempo_vida', models.IntegerField(verbose_name='Tiempo de vida')),
                ('frecuencia_man', models.IntegerField(verbose_name='Frecuencia de mantenimiento')),
                ('idconfiguracion_implemento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='componente_pieza.configuraciontipoimplemento', verbose_name='Configuracion')),
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
                ('horasdeuso', models.FloatField(default=0, verbose_name='Horas de uso')),
                ('codimplemento', models.CharField(max_length=12, verbose_name='Codigo de Implemento')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('estado_actividad', models.BooleanField(default=True, verbose_name='Estado Actividad')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
                ('idceco', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='ceco.ceco', verbose_name='Ceco')),
                ('idtipoimplemento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='implemento.tipoimplemento', verbose_name='Tipo Implemento')),
            ],
            options={
                'verbose_name': 'Implemento',
                'verbose_name_plural': 'Implementos',
                'ordering': ['implemento', 'idtipoimplemento'],
            },
        ),
    ]
