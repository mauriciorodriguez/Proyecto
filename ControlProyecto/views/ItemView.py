from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from ControlProyecto.models import Item, Estado
from django.urls.base import reverse_lazy
from django.http.response import HttpResponseRedirect
import datetime

class ItemView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["estados"] = Estado.objects.filter(item__id=kwargs["pk"]).order_by("fecha")
        return context
    template_name = "item.html"

class ItemCreateView(CreateView):
    model = Item
    fields = "__all__"
    template_name = "form_item.html"
    success_url = reverse_lazy('listado-item')
    def form_valid(self, form):
        self.object = form.save()
        e = Estado.objects.create(inicial=True, fecha=datetime.date.today(), item=self.object, nombre="Inicial") 
        e.save();     
        return HttpResponseRedirect(self.get_success_url())

class ItemUpdateView(UpdateView):
    model = Item
    fields = "__all__"
    template_name = "form_item.html"    

class ItemDeleteView(DeleteView):
    model = Item
    template_name = "borrar_item.html"
    success_url = reverse_lazy('listado-item')

class ItemListView(ListView):
    model = Item
    ordering = ["proyecto_id"]
    queryset = Item.objects.all()
    context_object_name = "items"
    paginate_by = 10
    template_name = "listado_item.html"
    