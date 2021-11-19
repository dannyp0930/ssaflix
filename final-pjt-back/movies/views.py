from types import coroutine
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Rank
from .forms import RankForm, SelectGenreForm
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-vote_average')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    ranks = movie.rank_set.all()
    user_rank = ranks.filter(user_id=request.user, movie_id=movie_pk)
    rank_form = RankForm()
    context = {
        'movie': movie,
        'ranks': ranks,
        'rank_form': rank_form,
        'user_rank': user_rank,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def create_rank(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rank_form = RankForm(request.POST)
    if rank_form.is_valid():
        rank = rank_form.save(commit=False)
        rank.movie = movie
        rank.user = request.user
        rank.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'rank_form': rank_form,
        'movie': movie,
        'ranks': movie.rank_set.all(),
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def delete_rank(request, movie_pk, rank_pk):
    if request.user.is_authenticated:
        rank = get_object_or_404(Rank, pk=rank_pk)
        if request.user == rank.user:
            rank.delete()
    return redirect('movies:detail', movie_pk)



def recommended(request):
    if request.user.is_authenticated:
        genre_form = SelectGenreForm(request.POST)
        if genre_form.is_valid():
            genre = genre_form.save(commit=False)
            genre.user = request.user
            genre.save()
            return redirect('movies:recomovie')
    else:
        genre_form = SelectGenreForm()
    context = {
        'genre_form': genre_form,
    }
    return render(request, 'movies/recommend.html', context)

def recomovie(request):
    pass
    
        
