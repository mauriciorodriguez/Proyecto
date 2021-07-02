from django.db import models

class Workflow(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.CharField(max_length=64, null=True)
    siguientes = models.ManyToManyField("self")