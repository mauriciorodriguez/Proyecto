# Generated by Django 3.2.3 on 2021-08-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0010_alter_estado_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
