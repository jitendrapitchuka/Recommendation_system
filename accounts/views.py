    
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,DetailView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import views as auth_views
from .models import movie,fav
from django.contrib.auth.models import User
from django.core.paginator import Paginator

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
   # movies_list=movie.objects.all()
    #return render(request, 'index.html',{'movies_list':movies_list})
    posts = movie.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 18)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'index.html', context)


class thankspage(TemplateView):
    template_name='logout.html'

class image_detailview(DetailView):

     model=movie


#class HomePage(TemplateView):
#    template_name='index.html'


