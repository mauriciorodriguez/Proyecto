from django.db import models
from django.contrib import admin
from ControlProyecto.models.ResponsablesEstado import ResponsablesEstadoInline

class Estado(models.Model):
    inicial = models.BooleanField()
    nombre = models.CharField(max_length=32)
    fecha = models.DateField()
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    responsables = models.ManyToManyField("Usuario", through="ResponsablesEstado", blank=True)
    siguiente = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ["fecha"]
    
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    inlines = (ResponsablesEstadoInline,)
    list_display = ("nombre", "item", "fecha")
    list_filter = ("responsables",)
    