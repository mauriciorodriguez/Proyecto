from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(null=True)
    usuarios = models.ManyToManyField("Usuario", through="RolUsuario")