from django.db import models


"""
Models based on data received from www.omdbapi.com
"""


class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.CharField(max_length=20, blank=True)
    rated = models.CharField(max_length=10, blank=True)
    released = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    director = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=1000, blank=True)
    actors = models.CharField(max_length=5000, blank=True)
    plot = models.TextField(blank=True)
    language = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    awards = models.CharField(max_length=200, blank=True)
    poster = models.CharField(max_length=200, blank=True)
    metascore = models.IntegerField(null=True, blank=True)
    imdbrating = models.DecimalField(max_digits=4,
                                     decimal_places=1,
                                     null=True, blank=True)
    imdbvotes = models.IntegerField(null=True, blank=True)
    imdbid = models.CharField(max_length=20, blank=True)
    type_picture = models.CharField(max_length=20, blank=True,
                                    verbose_name='type')
    dvd = models.DateField(null=True, blank=True)
    boxoffice = models.CharField(max_length=20, blank=True)
    production = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=200, blank=True)
    totalseasons = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    source = models.CharField(max_length=100, blank=True)
    value = models.CharField(max_length=20, blank=True)
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    def __str__(self):
        return f'{self.source} ({self.movie.title})'


class Comment(models.Model):
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()

    def __str__(self):
        return f'comment id: {self.id}, movie {self.movie.title}'