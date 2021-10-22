from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import views as auth_views
from .models import movie

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('templates/login')
    template_name='signup.html'


def Homepage(request):
    movies_list=movie.objects.all()

    return render(request, 'index.html',{'movies_list':movies_list})


class thankspage(TemplateView):
    template_name='logout.html'

class image_detailview(DetailView):
    model=movie


#class HomePage(TemplateView):
#    template_name='index.html'




