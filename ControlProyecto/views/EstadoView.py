from django.views.generic.edit import CreateView, UpdateView
from ControlProyecto.models import Estado
from django.urls.base import reverse_lazy
import datetime
from django.http.response import HttpResponseRedirect

class EstadoCreateView(CreateView):
    model = Estado
    fields = ["nombre", "item"]
    template_name = "form_estado.html"    
    success_url = reverse_lazy('listado-item')
    def form_valid(self, form):
        self.object = form.save()
        self.object.fecha = datetime.date.today()   
        self.object.inicial = False     
        self.object.save();     
        return HttpResponseRedirect(self.get_success_url())
    
class EstadoUpdateView(UpdateView):
    model = Estado
    fields = "__all__"
    template_name = "form_estado.html"