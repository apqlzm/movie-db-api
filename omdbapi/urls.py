from django.urls import path

from omdbapi import views

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/',
         views.UpdateDeleteMovieView.as_view(), name='update_delete_movie'),
    path('comments/', views.CommentView.as_view(), name='comments'),
    path('top/', views.top, name='top'),
]
