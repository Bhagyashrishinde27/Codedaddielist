from django.contrib import admin
from MovieApp.models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'type_of_movie', 'release_date', 'language', 'cast_name', 'producer_name', 'director_name']


admin.site.register(Movie,MovieAdmin)