from django.db import models
from django.contrib import admin
from django.urls.base import reverse

class ResponsablesEstado(models.Model):
    fecha = models.DateField()
    estado = models.ForeignKey("Estado", on_delete=models.CASCADE)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return ""
    def get_absolute_url(self):
        return reverse('listado-item')
    class Meta:
        ordering = ["fecha"]
    
class ResponsablesEstadoInline(admin.TabularInline):
    model = ResponsablesEstado
    extra = 1