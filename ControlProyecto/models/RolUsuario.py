from django.db import models

class RolUsuario(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    proyecto = models.ForeignKey("Proyecto", on_delete=models.CASCADE)
    rol = models.CharField(max_length=32)