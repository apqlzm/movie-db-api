from django.urls import path

from omdbapi import views

urlpatterns = [
    path('movies/', views.movies, name='api_find_trains'),
    path('movies/<int:movie_id>/', views.UpdateDeleteMovie.as_view()),
]
