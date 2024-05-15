# Generated by Django 4.2.10 on 2024-05-14 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('idcomponente', models.AutoField(primary_key=True, serialize=False)),
                ('componente', models.CharField(max_length=45, unique=True, verbose_name='Componente')),
                ('codcomponente', models.CharField(max_length=12, unique=True, verbose_name='Código componente')),
                ('tiempovida', models.IntegerField(verbose_name='Tiempo de vida')),
                ('frecuencia_man', models.IntegerField(blank=True, null=True, verbose_name='Frecuencia de mantenimiento')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Componente',
                'verbose_name_plural': 'Componentes',
                'ordering': ['componente'],
            },
        ),
        migrations.CreateModel(
            name='ConfiguracionTipoImplemento',
            fields=[
                ('idconfiguraciontipoimplemento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_configuracion', models.CharField(max_length=45, verbose_name='Configuracion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Configuracion Tipo Implemento',
                'verbose_name_plural': 'Configuraciones Tipo Implementos',
            },
        ),
        migrations.CreateModel(
            name='DetalleComponente',
            fields=[
                ('iddetallecomponente', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_piezas', models.IntegerField(default=1, verbose_name='Cantidad de piezas')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idcomponente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componente_pieza.componente', verbose_name='Componente')),
            ],
            options={
                'verbose_name': 'Detalles Componente',
                'verbose_name_plural': 'Detalles Componentes',
            },
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('idpieza', models.AutoField(primary_key=True, serialize=False)),
                ('pieza', models.CharField(max_length=45, unique=True, verbose_name='Pieza')),
                ('codpieza', models.CharField(max_length=12, unique=True, verbose_name='Codigo de pieza')),
                ('frecuencia_man', models.IntegerField(verbose_name='Frecuencia de mantenimiento de pieza')),
                ('tiempovida', models.IntegerField(verbose_name='Tiempo de vida de la pieza')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('creado_en', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado_en', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Pieza',
                'verbose_name_plural': 'Piezas',
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('idsistema', models.AutoField(primary_key=True, serialize=False)),
                ('sistema', models.CharField(max_length=45, unique=True, verbose_name='Sistema')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['sistema'],
            },
        ),
        migrations.CreateModel(
            name='DetalleConfiguracion',
            fields=[
                ('iddetalleconfiguracion', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('idconfiguraciontipoimplemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componente_pieza.configuraciontipoimplemento', verbose_name='Configuracion')),
                ('iddetallecomponente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componente_pieza.detallecomponente', verbose_name='Componente')),
            ],
            options={
                'verbose_name': 'Detalle Configuracion',
                'verbose_name_plural': 'Detalle Configuraciones',
            },
        ),
        migrations.AddField(
            model_name='detallecomponente',
            name='idpieza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componente_pieza.pieza', verbose_name='Pieza'),
        ),
        migrations.AddField(
            model_name='componente',
            name='idsistema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componente_pieza.sistema', verbose_name='Sistema'),
        ),
    ]
