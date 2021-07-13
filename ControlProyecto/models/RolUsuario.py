from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class RolUsuario(models.Model):
    
    class TipoRol(models.TextChoices):
        lider_tecnico = "LT", _("Lider Tecnico")
        lider_funcional = "LF", _("Lider Funcional")
        representante_cliente = "RC", _("Representante Cliente")
    
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    proyecto = models.ForeignKey("Proyecto", on_delete=models.CASCADE)
    rol = models.CharField(max_length=2, choices=TipoRol.choices, null=True)
    def __str__(self):
        return ""
    
class RolUsuarioInline(admin.TabularInline):
    model = RolUsuario
    extra = 1