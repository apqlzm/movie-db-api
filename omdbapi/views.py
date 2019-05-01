from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .omdb_data_fetcher import get_movie_data


@api_view(['POST'])
def movies(request):
    if request.method == 'POST':
        if 'title' not in request.data:
            return Response({'Error': 'title field required'})

        # TODO: firstly check in database if movie exists   
        movie_data = get_movie_data(request.data.get('title'))

        return Response(movie_data)
