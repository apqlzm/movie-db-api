from django.urls import path

from omdbapi import views

urlpatterns = [
    path('movies/', views.movies, name='api_find_trains'),
]
