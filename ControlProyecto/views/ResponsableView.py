from django.views.generic.edit import UpdateView, CreateView
from ControlProyecto.models import ResponsablesEstado
from django.urls.base import reverse_lazy

class ResponsableCreateView(CreateView):
    model = ResponsablesEstado
    fields = "__all__"
    template_name = "form_responsable.html"
    success_url = reverse_lazy('listado-item')

class ResponsableUpdateView(UpdateView):
    model = ResponsablesEstado
    fields = "__all__"
    template_name = "form_responsable.html"