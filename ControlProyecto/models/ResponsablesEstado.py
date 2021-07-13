from django.db import models
from django.contrib import admin

class ResponsablesEstado(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    estado = models.ForeignKey("Estado", on_delete=models.CASCADE)
    def __str__(self):
        return ""
    
class ResponsablesEstadoInline(admin.TabularInline):
    model = ResponsablesEstado
    extra = 1