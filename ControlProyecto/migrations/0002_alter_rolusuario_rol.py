# Generated by Django 3.2.3 on 2021-07-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolusuario',
            name='rol',
            field=models.CharField(choices=[('LT', 'Lider Tecnico'), ('LF', 'Lider Funcional'), ('RC', 'Representante Cliente')], max_length=2, null=True),
        ),
    ]
