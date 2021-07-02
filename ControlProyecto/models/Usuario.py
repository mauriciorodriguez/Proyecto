from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    dni = models.CharField(max_length=16)
    proyectos = models.ManyToManyField("Proyecto", through="RolUsuario")