from django.contrib import admin

from .models import Movie, Rating, Comment

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Comment)