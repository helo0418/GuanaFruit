from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect

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

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Insumo.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Insumos'
        context['create_url'] = reverse_lazy('erp:insumo_create')
        context['list_url'] = reverse_lazy('erp:insumo_list')
        context['entity'] = 'Insumos'

        print(reverse_lazy('erp:insumo_list'))
        return context


class InsumoCreateView(CreateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'Insumo/create.html'
    success_url = reverse_lazy('erp:insumo_list')

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un insumo'
        context['entity'] = 'Insumos'
        context['list_url'] = reverse_lazy('erp:insumo_list')
        context['action'] = 'add'
        return context


class InsumoUpdateView(UpdateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'Insumo/create.html'
    success_url = reverse_lazy('erp:insumo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar insumo'
        context['entity'] = 'Insumos'
        context['list_url'] = reverse_lazy('erp:insumo_list')
        context['action'] = 'edit'
        return context



class InsumoDeleteView(DeleteView):
    model = Insumo
    template_name = 'Insumo/delete.html'
    success_url = reverse_lazy('erp:insumo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar insumo'
        context['entity'] = 'Insumos'
        context['list_url'] = reverse_lazy('erp:insumo_list')
        return context








