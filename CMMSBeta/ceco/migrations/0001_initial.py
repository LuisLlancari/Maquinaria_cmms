# Generated by Django 4.2.10 on 2024-05-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ceco',
            fields=[
                ('idceco', models.AutoField(primary_key=True, serialize=False)),
                ('ceco', models.CharField(max_length=30, verbose_name='Ceco')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Ceco',
                'verbose_name_plural': 'Cecos',
            },
        ),
    ]
