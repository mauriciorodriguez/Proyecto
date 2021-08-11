from django.db import models
from django.contrib import admin
from ControlProyecto.models.RolUsuario import RolUsuarioInline
from ControlProyecto.models.ResponsablesEstado import ResponsablesEstadoInline
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

class Usuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dni = models.CharField(max_length=16, unique=True)
    proyectos = models.ManyToManyField("Proyecto", through="RolUsuario")
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
    
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = (RolUsuarioInline, ResponsablesEstadoInline)
    list_display = ("last_name","dni")
    def last_name(self, x):
        return x.user.last_name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(instance)
    instance.usuario.save()