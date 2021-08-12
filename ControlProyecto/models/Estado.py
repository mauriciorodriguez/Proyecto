from django.db import models
from django.contrib import admin
from ControlProyecto.models.ResponsablesEstado import ResponsablesEstadoInline
from django.urls.base import reverse

class Estado(models.Model):
    inicial = models.BooleanField(null=True)
    nombre = models.CharField(max_length=32)
    fecha = models.DateField(null=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    responsables = models.ManyToManyField("Usuario", through="ResponsablesEstado", blank=True)
    siguiente = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.pk) + ": " + self.nombre
    def get_absolute_url(self):
        return reverse('listado-item')
    class Meta:
        ordering = ["fecha"]
    
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    inlines = (ResponsablesEstadoInline,)
    list_display = ("nombre", "item", "fecha")
    list_filter = ("responsables",)
    