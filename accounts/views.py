    
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.views.generic import TemplateView,CreateView,DetailView,View
from django.urls import reverse_lazy,reverse
from . import forms
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .models import movie,fav
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('accounts:login')
    template_name='signup.html'


def add_movie(request,pk):
    
    # if fav.objects.filter(movie=pk,user=request.user.pk).exists():
    #    fav.objects.filter(movie=pk,user=request.user.pk).delete()
    # else:
        
    #     print(request.user.id)
    #     user=User.objects.filter(id=request.user.id)
    #     print(user)
    #     fav(movie=pk,user=user).save()
    
    # return HttpResponseRedirect('accounts/movie_detail.html')
    if fav.objects.filter(movie=pk,user=request.user.pk).exists():
        fav.objects.filter(movie=pk,user=request.user.pk).delete()
        messages.success(request, 'Removed from list.')
    else:
        
        print(request.user.id)
        movie_obj = movie.objects.filter(index=pk).first()
        user=User.objects.filter(id=request.user.id).first()
        print(user)
        fav_obj = fav(movie=movie_obj,user=user)
        messages.success(request, 'Added to list.')
        fav_obj.save()
    return redirect('detail',pk)


def search_results(request):
    if request.method=='POST':
        searched=request.POST['searched']
        movies_obj=movie.objects.filter(title__contains=searched)
        return render(request, 'search.html',{'movies_obj':movies_obj})
    else:
        
        return render(request, 'search.html',{})





def my_list(request):
    
    temp=fav.objects.filter(user__id=request.user.id)
    
    return render(request, 'my_list.html',{'temp':temp})


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
    context = {'page_obj': page_obj,'posts':posts}
    # sending the page object to index.html
    return render(request, 'index.html', context)


class thankspage(TemplateView):
    template_name='logout.html'


class image_detailview(View):

    movie = movie
    def get(self, request, pk):
        movies_detail = self.movie.objects.get(pk=pk)
        print(movies_detail)

        # Create your connection.
        cnx = sqlite3.connect('db.sqlite3')

        df = pd.read_sql_query("SELECT * FROM accounts_movie", cnx)
        #print(df.head())
        features = ['genres', 'title','text']
        for f in features:
            df[f] = df[f].fillna('')

        
        def combineFeatures(row):
            return row['genres'] + " " + row['title']+" "+row['text']

        df['combineFeatures'] = df.apply(combineFeatures, axis = 1)
        print(df['combineFeatures'])
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df['combineFeatures'])
        cosine_sim = cosine_similarity(count_matrix)
        

        movie_obj = self.movie.objects.filter(index=pk).first()
        movie_user_likes=movie_obj.title
        print(movie_user_likes)
    
    

        def get_index_from_title(title):
            return df[df.title == title]["index"].values[0]

        movie_index = get_index_from_title(movie_user_likes)
        print(movie_index)

        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)

        def get_title_from_index(index):
            return df[df.index == index]["index"].values[0]
        i=0
        li=[]
        for x in sorted_similar_movies:
            get_index = get_title_from_index(x[0])
            
            recommendation_list_obj=movie.objects.get(index=get_index)
            
            li.append(recommendation_list_obj)


            print(get_title_from_index(x[0]))
            i=i+1
            if i>17:
                break
        print(li)
        return render(request,'accounts/movie_detail.html',{'li':li,'movie':movies_detail})





#class HomePage(TemplateView):
#    template_name='index.html'

