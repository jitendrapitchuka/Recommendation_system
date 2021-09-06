from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from . import forms

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('templates/login')
    template_name='signup.html'

class user_page(TemplateView):
    template_name='user_page.html'


class thankspage(TemplateView):
    template_name='logout.html'

class HomePage(TemplateView):
    template_name='index.html'


