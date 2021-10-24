from django.db import models
from django.contrib.auth.models import User


#class User(auth.models.User,auth.models.PermissionsMixin):

#    def __str__(self):
 #       return (self.username)






class movie(models.Model):
    index=models.IntegerField(primary_key=True)
    movie_id=models.IntegerField()
    title=models.CharField(max_length=120)
    genres=models.CharField(max_length=130)
    imdb_id=models.IntegerField()
    tmdb_id=models.IntegerField()
    Image_url=models.URLField(max_length=200)
    text=models.TextField(max_length=400)

class fav(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(movie, on_delete=models.CASCADE)