from django.views.generic.edit import UpdateView
from ControlProyecto.models import RolUsuario

class RolUpdateView(UpdateView):
    model = RolUsuario
    fields = "__all__"
    template_name = "rol_usuario.html"