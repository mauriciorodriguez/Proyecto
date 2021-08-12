from django.views.generic.edit import CreateView, UpdateView
from ControlProyecto.models import Workflow
from django.views.generic.list import ListView
from django.urls.base import reverse_lazy

class WorkflowCreateView(CreateView):
    model = Workflow
    fields = "__all__"
    template_name = "form_workflow.html"
    success_url = reverse_lazy('listado-workflow')
    
class WorkflowUpdateView(UpdateView):
    model = Workflow
    fields = "__all__"
    template_name = "form_workflow.html"
    
class WorkflowListView(ListView):
    model = Workflow
    ordering = ["inicial", "nombre"]
    queryset = Workflow.objects.all()
    context_object_name = "workflows"
    paginate_by = 10
    template_name = "listado_workflow.html"