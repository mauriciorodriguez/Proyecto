from django.db import models
from django.contrib import admin
from ControlProyecto.models.RolUsuario import RolUsuarioInline

class Proyecto(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(null=True)
    usuarios = models.ManyToManyField("Usuario", through="RolUsuario")
    def __str__(self):
        return self.nombre
    
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    inlines = (RolUsuarioInline,)