from django.urls import path

from omdbapi import views

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.UpdateDeleteMovieView.as_view()),
    path('comments/', views.CommentView.as_view()),
    path('top/', views.top),
]
