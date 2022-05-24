from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, FormView, UpdateView, ListView

from .models import Persona
from .forms import PersonaForm
# Create your views here.

class Educacion(TemplateView):
    template_name = 'educacion.html'


class PersonaListView(ListView):
    model = Persona
    pagininate_by = 25
    template_name = 'persona_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['dato'] = 'testeo'

        return context

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    #fields = ['nombrePersona', 'apellidoPersona']
    template_name = 'persona_update_form.html'
    #success_url: 'direccion:Educacion'
    success_url = reverse_lazy('direccion:educacion')

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona_form.html'
    success_url = reverse_lazy('direccion:educacion')