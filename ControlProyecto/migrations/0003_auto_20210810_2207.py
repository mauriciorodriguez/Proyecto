# Generated by Django 3.2.3 on 2021-08-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlProyecto', '0002_alter_workflow_anterior'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflow',
            name='anterior',
        ),
        migrations.AddField(
            model_name='workflow',
            name='siguientes',
            field=models.ManyToManyField(blank=True, null=True, to='ControlProyecto.Workflow'),
        ),
    ]
