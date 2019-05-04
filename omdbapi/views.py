from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from omdbapi.models import Movie, Comment
from omdbapi.serializers import MovieSerializer, CommentSerializer

from .utils.crud_helpers import (create_new_movie, find_movie_in_db,
                                 get_all_movies, prepare_top_list)
from .utils.omdb_data_fetcher import get_movie_data


@api_view(['POST', 'GET'])
def movies(request):
    if request.method == 'POST':

        if 'title' not in request.data:
            return HttpResponseBadRequest({'title is required'})

        title = request.data['title']
        movie = find_movie_in_db(title)
        if not movie:
            movie_data = get_movie_data(title)
            if movie_data == {}:
                return HttpResponseNotFound('Movie could not be fetched from external database')
            movie = create_new_movie(movie_data)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'GET':
        all_movies = get_all_movies()
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def top(request):
    if request.method == 'GET':
        if 'date_from' not in request.GET or 'date_to' not in request.GET:
            return HttpResponseBadRequest({'date_from and date_to query params are required'})
        
        date_from = request.GET['date_from']
        date_to = request.GET['date_to']

        try:
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
        except ValueError:
            return HttpResponseBadRequest('date_from has wrong format. Use this one instead: YYYY-MM-DD.')

        try:
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            return HttpResponseBadRequest('date_to has wrong format. Use this one instead: YYYY-MM-DD.')

        top_list = prepare_top_list(date_from, date_to)
        return Response(top_list)


class UpdateDeleteMovieView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        movie_id = self.request.query_params.get('movie_id')
        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset
