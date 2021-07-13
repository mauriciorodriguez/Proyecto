from django.db import models
from django.contrib import admin

class TipoItem(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
    workflow = models.OneToOneField("Workflow", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
@admin.register(TipoItem)
class TipoItemAdmin(admin.ModelAdmin):
    list_display = ["nombre", "workflow"]
    list_filter = ("workflow", )
    ordering = ("nombre", )