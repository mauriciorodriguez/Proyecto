"""TPIntegradorLPyL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ControlProyecto.views import indexView, ProyectoListView, ProyectoCreateView, ProyectoView, ProyectoUpdateView, ProyectoDeleteView, ItemView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemListView, WorkflowCreateView, WorkflowListView, RolUpdateView, WorkflowUpdateView, UsuarioListView, UsuarioView, EstadoCreateView, EstadoUpdateView
from ControlProyecto.views.ResponsableView import ResponsableUpdateView,\
    ResponsableCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', indexView.as_view(), name="inicio"),
    path('proyectos/', ProyectoListView.as_view(), name="listado-proyecto"),
    path('proyectos/<int:pk>/', ProyectoView.as_view(), name="detalle-proyecto"),    
    path('proyectos/<int:pk>/editar/', ProyectoUpdateView.as_view(), name="editar-proyecto"),
    path('proyectos/<int:pk>/borrar/', ProyectoDeleteView.as_view(), name="borrar-proyecto"),
    path('proyectos/crear/', ProyectoCreateView.as_view(), name="crear-proyecto"),
    path('item/crear/', ItemCreateView.as_view(), name="crear-item"),
    path('item/<int:pk>/', ItemView.as_view(), name="detalle-item"),
    path('item/<int:pk>/editar/', ItemUpdateView.as_view(), name="editar-item"),
    path('item/<int:pk>/borrar/', ItemDeleteView.as_view(), name="borrar-item"),
    path('item/', ItemListView.as_view(), name="listado-item"),
    path('rol/<int:pk>/', RolUpdateView.as_view(), name="rol-usuario"),
    path('workflow/crear/', WorkflowCreateView.as_view(), name="crear-workflow"), 
    path('workflow/<int:pk>/editar/', WorkflowUpdateView.as_view(), name="editar-workflow"), 
    path('workflow/', WorkflowListView.as_view(), name="listado-workflow"),  
    path('usuario/', UsuarioListView.as_view(), name="listado-usuario"), 
    path('usuario/<int:pk>/', UsuarioView.as_view(), name="detalle-usuario"), 
    path('estado/crear', EstadoCreateView.as_view(), name="crear-estado"), 
    path('estado/<int:pk>/editar/', EstadoUpdateView.as_view(), name="editar-estado"),
    path('responsable/<int:pk>/editar/', ResponsableUpdateView.as_view(), name="editar-responsable"),
    path('responsable/crear', ResponsableCreateView.as_view(), name="crear-responsable"),
]
