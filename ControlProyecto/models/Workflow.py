from django.db import models
from django.contrib import admin

class Workflow(models.Model):
    inicial = models.BooleanField()
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(null=True)
    siguientes = models.ManyToManyField("self", blank=True)
    def __str__(self):           
        return self.nombre
    
@admin.register(Workflow)
class WorklfowAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    list_filter = ("inicial",)
    filter_horizontal = ("siguientes",)
    ordering = ("nombre",)