from django.shortcuts import render
from MovieApp.models import Movie
from django.views.generic import ListView, DetailView


# Create your views here.
def show(request):
    return render(request,'movieapp/index.html')

# def displyDetail(request):
#     # ms = Movie.objects.get(id=id)
#     ms = Movie.objects.all()
#     dic = {"ms": ms}
#     print(dic)
#     return render(request, 'movieapp/details.html', context=dic)

class MovieList(ListView):
    model = Movie

class MovieDetail(DetailView):
    model = Movie



# def detail_info(request,id=id):
#     # ms = Movie.objects.filter(movie_name__iexact="Dabbang1")
#     ms = Movie.objects.get(id=id)
#     dict = {'ms': ms}
#     return render(request, 'movieapp/details.html', context=dict)
#

