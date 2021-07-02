from django.db import models

class Estado(models.Model):
    nombre = models.CharField(max_length=32)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    responsables = models.ManyToManyField("Usuario", through="ResponsablesEstado")
    siguiente = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    primerEstado = models.BooleanField()