from django.db import models

class ResponsablesEstado(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    estado = models.ForeignKey("Estado", on_delete=models.CASCADE)