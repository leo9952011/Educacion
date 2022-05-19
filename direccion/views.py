from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class Educacion(TemplateView):
    template_name = 'educacion.html'