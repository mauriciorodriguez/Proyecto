from django.db import models
from django.contrib import admin
from django.urls.base import reverse

class Workflow(models.Model):
    inicial = models.BooleanField()
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(blank=True)
    siguientes = models.ManyToManyField("self", blank=True, symmetrical=False)
    def __str__(self):           
        return self.nombre
    def get_absolute_url(self):
        return reverse('listado-workflow')
    
@admin.register(Workflow)
class WorklfowAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    list_filter = ("inicial",)
    filter_horizontal = ("siguientes",)
    ordering = ("nombre",)