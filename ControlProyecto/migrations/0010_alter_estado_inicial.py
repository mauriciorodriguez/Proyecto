# Generated by Django 3.2.3 on 2021-08-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0009_alter_tipoitem_workflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='inicial',
            field=models.BooleanField(null=True),
        ),
    ]
