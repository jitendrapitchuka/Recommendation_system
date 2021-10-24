    
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,DetailView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import views as auth_views
from .models import movie,fav
from django.contrib.auth.models import User

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('templates/login')
    template_name='signup.html'


def add_movie(request,pk):
    
    if fav.objects.filter(movie=pk,user=request.user.pk).exists():
       fav.objects.filter(movie=pk,user=request.user.pk).delete()
    else:
        
        print(request.user.id)
        user=User.objects.filter(id=request.user.id)
        print(user)
        fav(movie=pk,user=user).save()
    
    return HttpResponseRedirect('accounts/movie_detail.html')



def my_list(request):
#    temp= .filter( =request.user)
  return render(request, 'my_list.html')

def Homepage(request):
    movies_list=movie.objects.all()
    
    return render(request, 'index.html',{'movies_list':movies_list})


class thankspage(TemplateView):
    template_name='logout.html'

class image_detailview(DetailView):

    model=movie


#class HomePage(TemplateView):
#    template_name='index.html'


