# Generated by Django 3.2.3 on 2021-07-13 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0007_auto_20210713_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='siguiente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.estado'),
        ),
    ]