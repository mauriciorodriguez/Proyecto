from django.db import models

class Item(models.Model):
    proyecto = models.ForeignKey("Proyecto",  on_delete=models.CASCADE)
    tipo = models.ForeignKey("TipoItem",  on_delete=models.CASCADE)
    descripcion = models.TextField()