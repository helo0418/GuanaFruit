from django.shortcuts import render
from django.views.generic import ListView, CreateView

from core.erp.models import Insumo
from core.erp.forms import InsumoForm


def insumo_list(request):
   data = {
        'insumos': Insumo.objects.all(),
        'titulo': 'listado de insumos',
    }
   return render(request, 'Insumo/list.html', data)

class InsumoListView(ListView):
    model = Insumo
    template_name = 'Insumo/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Insumos'
        return context


class InsumoCreateView(CreateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'Insumo/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un insumo'
        return context
