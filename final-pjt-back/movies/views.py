from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-vote_average')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def recommended(request):
    pass