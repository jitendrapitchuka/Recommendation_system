"""recommendation_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from accounts import views
from accounts.views import image_detailview

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.HomePage.as_view(),name='home'),
    path('accounts/',include('accounts.urls')),
     #path('user_page/',views.user_loginpage,name='user_page'),
    path('thanks/',views.thankspage.as_view(),name='thanks'),
    path('',views.Homepage,name='homepage'),
   path('movie/<int:pk>/', views.image_detailview.as_view(),name='detail'),
  path('<int:pk>/',views.add_movie,name="movie_add"),
    path('list/',views.my_list,name='my_list'),
]
