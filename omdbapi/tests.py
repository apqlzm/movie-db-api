from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from omdbapi import models
import json


class MovieTests(APITestCase):
    def setUp(self):
        models.Movie.objects.create(title='Some title', imdbid='123asd')

    def test_list_movies(self):
        """ tests GET /movies """

        url = reverse('movies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content), [
                {'id': 1,
                 'title': 'Some title',
                 'year': '',
                 'rated': '',
                 'released': None,
                 'runtime': None,
                 'genre': '',
                 'director': '',
                 'writer': '',
                 'actors': '',
                 'plot': '',
                 'language': '',
                 'country': '',
                 'awards': '',
                 'poster': '',
                 'metascore': None,
                 'imdbrating': None,
                 'imdbvotes': None,
                 'imdbid': '123asd',
                 'type_picture': '',
                 'dvd': None,
                 'boxoffice': '',
                 'production': '',
                 'website': '',
                 'totalseasons': None,
                 'ratings': []}
            ]
        )

    # def test_create_movie(self):
    #     """ tests POST /movies """

    #     url = reverse('movies')
    #     data = {'title': 'Django'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Movie.objects.count(), 1)
