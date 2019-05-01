from django.db import models

# TODO:
# runtime stored as minutes
# make fields optional instead of title


class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.IntegerField(default=None)
    rated = models.CharField(max_length=10, default='N/A')
    released = models.DateField(default=None)
    runtime = models.IntegerField(default=None)
    genre = models.CharField(max_length=100, default='N/A')
    director = models.CharField(max_length=100, default='N/A')
    writer = models.CharField(max_length=100, default='N/A')
    actors = models.CharField(max_length=5000, default='N/A')
    plot = models.TextField()
    language = models.CharField(max_length=100, default='N/A')
    country = models.CharField(max_length=100, default='N/A')
    awards = models.CharField(max_length=200, default='N/A')
    poster = models.CharField(max_length=200, default='N/A')
    metascore = models.IntegerField(default=None)
    imdbrating = models.DecimalField(decimal_places=1, default=None)
    imdbvotes = models.IntegerField(default=None)
    imdbid = models.CharField(max_length=20, default='N/A')
    type_ = models.CharField(max_length=20, default='N/A')
    dvd = models.DateField(default=None)
    boxoffice = models.CharField(max_length=20, default='N/A')
    production = models.CharField(max_length=50, default='N/A')
    website = models.CharField(max_length=200, default='N/A')


class Rating(models.Model):
    source = models.CharField(max_length=100, default='N/A')
    value = models.CharField(max_length=20, default='N/A')
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE
    )
