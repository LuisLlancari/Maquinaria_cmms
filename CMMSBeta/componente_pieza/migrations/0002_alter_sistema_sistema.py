# Generated by Django 4.2.10 on 2024-07-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componente_pieza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistema',
            name='sistema',
            field=models.CharField(max_length=45, verbose_name='Sistema'),
        ),
    ]
