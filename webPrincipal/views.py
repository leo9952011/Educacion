from django.shortcuts import render

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Home(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect'
    succes_url = 'principal:home'
    template_name = 'home.html'


