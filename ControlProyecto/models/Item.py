from django.db import models
from django.contrib import admin
from django.urls.base import reverse

class Item(models.Model):
    proyecto = models.ForeignKey("Proyecto",  on_delete=models.CASCADE)
    tipo = models.ForeignKey("TipoItem",  on_delete=models.CASCADE)
    descripcion = models.TextField()
    def get_absolute_url(self):
        return reverse('detalle-item', kwargs={'pk': self.pk})
    def __str__(self):
        return self.tipo.nombre
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["tipo", "proyecto", "descripcion"]
    list_filter = ("proyecto", "tipo", )
    ordering = ("proyecto", )