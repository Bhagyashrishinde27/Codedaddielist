from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    type_of_movie = models.CharField(max_length=40)
    release_date = models.DateTimeField(max_length=50)
    language= models.CharField(max_length=20)
    cast_name=models.CharField(max_length=40)
    producer_name= models.CharField(max_length=20)
    director_name = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

