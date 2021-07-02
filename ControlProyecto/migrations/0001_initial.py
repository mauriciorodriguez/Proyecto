# Generated by Django 3.2.3 on 2021-07-02 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('primerEstado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RolUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=32)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('descripcion', models.CharField(max_length=64, null=True)),
                ('siguientes', models.ManyToManyField(related_name='_ControlProyecto_workflow_siguientes_+', to='ControlProyecto.Workflow')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('dni', models.CharField(max_length=16)),
                ('proyectos', models.ManyToManyField(through='ControlProyecto.RolUsuario', to='ControlProyecto.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32, unique=True)),
                ('workflow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.workflow')),
            ],
        ),
        migrations.AddField(
            model_name='rolusuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.usuario'),
        ),
        migrations.CreateModel(
            name='ResponsablesEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.estado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuarios',
            field=models.ManyToManyField(through='ControlProyecto.RolUsuario', to='ControlProyecto.Usuario'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.proyecto')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.tipoitem')),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.item'),
        ),
        migrations.AddField(
            model_name='estado',
            name='responsables',
            field=models.ManyToManyField(through='ControlProyecto.ResponsablesEstado', to='ControlProyecto.Usuario'),
        ),
        migrations.AddField(
            model_name='estado',
            name='siguiente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlProyecto.estado'),
        ),
    ]