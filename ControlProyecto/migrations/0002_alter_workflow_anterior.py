# Generated by Django 3.2.3 on 2021-08-11 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='anterior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.workflow'),
        ),
    ]
