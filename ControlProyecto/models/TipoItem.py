from django.db import models

class TipoItem(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
    workflow = models.OneToOneField("Workflow", on_delete=models.CASCADE)