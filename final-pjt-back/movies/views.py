from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Rank, SelectGenre
from .forms import RankForm, SelectGenreForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-popularity')
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



# def recommended(request):
#     if request.user.is_authenticated:
#         genre_form = SelectGenreForm(request.POST)
#         if genre_form.is_valid():
#             genre = genre_form.save(commit=False)
#             genre.user = request.user
#             genre.save()
            
#             movies = Movie.objects.prefetch_related('genres').filter(genres__in=[genre.selected_genre]).order_by('-vote_average').distinct()[:3]
#             print(movies)
#             context = {
#                 'movies': movies,
#             }
#             return render(request, 'movies/recommended.html', context)
#     else:
#         genre_form = SelectGenreForm()
#     context = {
#         'genre_form': genre_form,
#     }
#     return render(request, 'movies/recommend.html', context)

import pandas as pd
import numpy as np

# 유저간 유사도 구하기 : 피어슨 상관계수
def pearson(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))

def recommended(request):
    # 유저의 평점 데이터 불러오기
    ranks = pd.DataFrame(data=Rank.objects.all().values('user', 'movie', 'rank'))
    ranks = ranks.rename(columns={'user':"userId", 'movie':"movieId"})

    # 영화 데이터에서 id값 가져오기
    movie = pd.DataFrame(data=Movie.objects.all().values('id'))
    movie = movie.rename(columns={'id':'movieId'})

    # 평가하지 않은 데이터는 NaN값으로
    movie.movieId = pd.to_numeric(movie.movieId, errors='coerce')
    ranks.movieId = pd.to_numeric(ranks.movieId, errors='coerce')

    # 데이터 통합 후 피벗 테이블 생성
    data = pd.merge(ranks, movie, on='movieId', how='inner')
    matrix = data.pivot_table(index='movieId', columns='userId', values='rank')
    result = []

    for side_id in matrix.columns:
        
        if side_id == request.user.id:
            continue
        
        # 유저간 유사도 검사
        cor = pearson(matrix[request.user.id], matrix[side_id])

        # 평점이 NaN 값이면 0으로 입력
        if np.isnan(cor):
            result.append((side_id, 0))
        else:
            result.append((side_id, cor))

    # 가장 유사한 유저 값 생성
    result = max(result, key=lambda r: -r[1])[0]

    # 자신이 평가한 영화 id값
    movies = Rank.objects.filter(user_id=request.user.id).values('movie_id')
    movies = [value['movie_id'] for value in movies]

    # 유사 유저가 평가한 영화 id값
    sim_movie = Rank.objects.filter(user_id=result).values('movie_id')
    
    # 내가 보지 않은 영화 id 후보 결정
    id_list = [value['movie_id'] for value in sim_movie if value['movie_id'] not in movies]
    recommends = Movie.objects.filter(id__in=id_list)

    # 사용자 기반 추천 영화가 없다면 인기도 순으로 3개
    if not recommends:
        recommends = Movie.objects.order_by('-popularity')[:2]
    context = {
        'recommends':recommends,
    }
    return render(request, 'movies/recommended.html', context)