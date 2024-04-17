# Generated by Django 5.0.3 on 2024-04-16 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tractor', '0003_alter_reportetractor_correlativo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportetractor',
            name='idusuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportes_tractor_tractor', to=settings.AUTH_USER_MODEL),
        ),
    ]
