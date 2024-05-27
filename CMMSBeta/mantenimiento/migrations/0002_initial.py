# Generated by Django 4.2.10 on 2024-05-25 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mantenimiento', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='persona',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='usuario.persona', verbose_name='Persona'),
        ),
    ]
