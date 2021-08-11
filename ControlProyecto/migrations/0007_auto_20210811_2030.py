# Generated by Django 3.2.3 on 2021-08-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0006_rename_primerestado_estado_inicial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado',
            options={'ordering': ['fecha']},
        ),
        migrations.AlterModelOptions(
            name='responsablesestado',
            options={'ordering': ['fecha']},
        ),
        migrations.AlterField(
            model_name='rolusuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('LT', 'Lider Tecnico'), ('LF', 'Lider Funcional'), ('RC', 'Representante Cliente')], max_length=2, null=True),
        ),
    ]
