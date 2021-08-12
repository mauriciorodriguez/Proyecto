from django.views.generic.list import ListView
from ControlProyecto.models import Usuario
from django.views.generic.base import TemplateView

class UsuarioListView(ListView):
    model = Usuario
    ordering = ["dni"]
    queryset = Usuario.objects.all()
    context_object_name = "usuarios"
    paginate_by = 10
    template_name = "listado_usuario.html"
    
class UsuarioView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["usuario"] = Usuario.objects.get(id=kwargs["pk"])
        return context
    template_name = "usuario.html"