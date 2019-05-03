

from django.http import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from omdbapi.serializers import MovieSerializer

from .utils.crud_helpers import (create_new_movie, find_movie_in_db,
                                 get_all_movies)
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
            movie = create_new_movie(movie_data)
        
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'GET':
        all_movies = get_all_movies()
        serializer = MovieSerializer(all_movies, many=True)
        return Response(serializer.data)
