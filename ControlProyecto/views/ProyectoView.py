from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ControlProyecto.models import Proyecto, RolUsuario, Item
from django.views.generic.base import TemplateView
from django.urls.base import reverse_lazy

class ProyectoView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["proyecto"] = Proyecto.objects.get(id=kwargs["pk"])
        context["roles"] = RolUsuario.objects.filter(proyecto__id=kwargs["pk"]).order_by("usuario__user__last_name")
        context["items"] = Item.objects.filter(proyecto__id=kwargs["pk"])
        return context
    template_name = "proyecto.html"

class ProyectoCreateView(CreateView):
    model = Proyecto
    fields = ["nombre", "descripcion"]
    template_name = "form_proyecto.html"
    success_url = reverse_lazy('listado-proyecto')

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    fields = "__all__"
    template_name = "form_proyecto.html"

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = "borrar_proyecto.html"
    success_url = reverse_lazy('listado-proyecto')

class ProyectoListView(ListView):
    model = Proyecto
    ordering = ["nombre"]
    queryset = Proyecto.objects.all()
    context_object_name = "proyectos"
    paginate_by = 10
    template_name = "listado_proyectos.html"