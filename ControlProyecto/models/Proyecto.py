from django.db import models
from django.contrib import admin
from ControlProyecto.models.RolUsuario import RolUsuarioInline
from django.urls.base import reverse

class Proyecto(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(null=True)
    usuarios = models.ManyToManyField("Usuario", through="RolUsuario", blank=True)
    def get_absolute_url(self):
        return reverse('detalle-proyecto', kwargs={'pk': self.pk})
    def __str__(self):
        return self.nombre
    
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    inlines = (RolUsuarioInline,)