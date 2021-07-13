from django.db import models
from django.contrib import admin
from ControlProyecto.models.RolUsuario import RolUsuarioInline
from ControlProyecto.models.ResponsablesEstado import ResponsablesEstadoInline

class Usuario(models.Model):
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    dni = models.CharField(max_length=16)
    proyectos = models.ManyToManyField("Proyecto", through="RolUsuario")
    def __str__(self):
        return self.nombre+" "+self.apellido
    
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = (RolUsuarioInline, ResponsablesEstadoInline)
    list_display = ["apellido", "nombre", "dni"]
    ordering = ("apellido", "nombre")