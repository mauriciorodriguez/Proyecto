# Generated by Django 3.2.3 on 2021-07-13 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0006_workflow_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='responsables',
            field=models.ManyToManyField(blank=True, through='ControlProyecto.ResponsablesEstado', to='ControlProyecto.Usuario'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='siguiente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.estado'),
        ),
    ]