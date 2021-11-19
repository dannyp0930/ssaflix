from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


RANK = [(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')]


class Rank(models.Model):
    rank = models.IntegerField(choices=RANK)
    content = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
GENRES = (
    (12, '모험'),
    (14, '판타지'),
    (16, '애니메이션'),
    (18, '드라마'),
    (27, '공포'),
    (28, '액션'),
    (35, '코미디'),
    (36, '역사'),
    (37, '서부'),
    (53, '스릴러'),
    (80, '범죄'),
    (99, '다큐멘터리'),
    (878, 'SF'),
    (9648, '미스터리'),
    (10402, '음악'),
    (10749, '로맨스'),
    (10751, '가족'),
    (10752, '전쟁'),
    (10770, 'TV 영화'),
)


class SelectGenre(models.Model):

    selected_genre = models.IntegerField(choices=GENRES)