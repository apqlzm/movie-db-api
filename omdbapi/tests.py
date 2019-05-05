from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from omdbapi import models
import json
from unittest.mock import patch
from datetime import datetime


MOVIE_DATA = {
    "Title": "Good Bye Lenin!",
    "Year": "2003",
    "Rated": "R",
    "Released": "14 May 2004",
    "Runtime": "121 min",
    "Genre": "Comedy, Drama, Romance",
    "Director": "Wolfgang Becker",
    "Writer": "Bernd Lichtenberg, Wolfgang Becker (author), Achim von Borries (collaborator on screenplay), Henk Handloegten (collaborator on screenplay), Chris Silber (collaborator on screenplay)",
    "Actors": "Daniel Brühl, Katrin Saß, Chulpan Khamatova, Maria Simon",
    "Plot": "In 1990, to protect his fragile mother from a fatal shock after a long coma, a young man must keep her from learning that her beloved nation of East Germany as she knew it has disappeared.",
    "Language": "German, English, Russian",
    "Country": "Germany",
    "Awards": "Nominated for 1 Golden Globe. Another 33 wins & 19 nominations.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BMTI0MTg4NzI3M15BMl5BanBnXkFtZTcwOTE0MTUyMQ@@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "7.7/10"
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": "90%"
        },
        {
            "Source": "Metacritic",
            "Value": "68/100"
        }
    ],
    "Metascore": "68",
    "imdbRating": "7.7",
    "imdbVotes": "128,447",
    "imdbID": "tt0301357",
    "Type": "movie",
    "DVD": "10 Aug 2004",
    "BoxOffice": "$4,000,000",
    "Production": "Sony Pictures Classics",
    "Website": "http://www.german-cinema.de/archive/film_view.php?film_id=939",
    "Response": "True"
}


def prepare_data():
    models.Movie.objects.create(
        title='Some title2', imdbid='223asd', plot='lorem ipsum2', id=2)
    models.Movie.objects.create(
        title='Some title3', imdbid='323asd', plot='lorem ipsum3', id=3)

    models.Comment.objects.create(
        body='x', movie_id=1)
    models.Comment.objects.create(
        body='x', movie_id=1)
    models.Comment.objects.create(
        body='x', movie_id=1)

    models.Comment.objects.create(
        body='x', movie_id=2)
    models.Comment.objects.create(
        body='x', movie_id=2)

    models.Comment.objects.create(
        body='x', movie_id=3)
    models.Comment.objects.create(
        body='x', movie_id=3)


class MovieTests(APITestCase):
    def setUp(self):
        models.Movie.objects.create(
            title='Some title', imdbid='123asd', plot='lorem ipsum')

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
                 'plot': 'lorem ipsum',
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

    @patch('omdbapi.utils.omdb_data_fetcher.get_movie_data')
    def test_create_movie(self, mock_get_movie_data):
        """ tests POST /movies """
        mock_get_movie_data.return_value = MOVIE_DATA

        url = reverse('movies')
        data = {'title': 'good bye lenin'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content), {'id': 2,
                                           'title': 'Good Bye Lenin!',
                                           'year': '2003',
                                           'rated': 'R',
                                           'released': '2004-05-14',
                                           'runtime': 121,
                                           'genre': 'Comedy, Drama, Romance',
                                           'director': 'Wolfgang Becker',
                                           'writer': 'Bernd Lichtenberg, Wolfgang Becker (author), Achim von Borries (collaborator on screenplay), Henk Handloegten (collaborator on screenplay), Chris Silber (collaborator on screenplay)', 'actors': 'Daniel Brühl, Katrin Saß, Chulpan Khamatova, Maria Simon',
                                           'plot': 'In 1990, to protect his fragile mother from a fatal shock after a long coma, a young man must keep her from learning that her beloved nation of East Germany as she knew it has disappeared.',
                                           'language': 'German, English, Russian',
                                           'country': 'Germany',
                                           'awards': 'Nominated for 1 Golden Globe. Another 33 wins & 19 nominations.',
                                           'poster': 'https://m.media-amazon.com/images/M/MV5BMTI0MTg4NzI3M15BMl5BanBnXkFtZTcwOTE0MTUyMQ@@._V1_SX300.jpg',
                                           'metascore': 68,
                                           'imdbrating': '7.7',
                                           'imdbvotes': 128447,
                                           'imdbid': 'tt0301357',
                                           'type_picture': 'movie',
                                           'dvd': '2004-08-10',
                                           'boxoffice': '$4,000,000',
                                           'production': 'Sony Pictures Classics',
                                           'website': 'http://www.german-cinema.de/archive/film_view.php?film_id=939',
                                           'totalseasons': None,
                                           'ratings': [
                                               {'id': 1, 'source': 'Internet Movie Database',
                                                   'value': '7.7/10'},
                                               {'id': 2, 'source': 'Rotten Tomatoes',
                                                   'value': '90%'},
                                               {'id': 3, 'source': 'Metacritic', 'value': '68/100'}]}
        )

    def test_delete_movie(self):
        """ tests DELETE /movies/<movie-id>/ """
        response = self.client.delete('/movies/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(models.Movie.objects.all()), 0)

    def test_update_movie(self):
        """ tests UPDATE /movies/<movie-id>/ """
        data = {'plot': 'aaa'}

        response = self.client.put('/movies/1/', data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Movie.objects.all()[0].plot, 'aaa')

    def test_create_comment(self):
        """ tests POST /comments """
        data = {
            "body": "Good film",
            "movie_id": 1
        }
        response = self.client.post('/comments/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(models.Comment.objects.all()), 1)

    def test_find_comment_by_movie_id(self):
        """ tests GET /comments """
        models.Comment.objects.create(
            body='lorem ipsum', movie_id=1)

        data = {
            "movie_id": 1
        }
        response = self.client.get('/comments/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content),
                         [{'id': 1, 'body': 'lorem ipsum', 'movie_id': 1}])

    def test_top(self):
        prepare_data()

        today = datetime.now().date().strftime('%Y-%m-%d')

        params = f'?date_from={today}&date_to={today}'

        response = self.client.get(f'/top/{params}')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(json.loads(response.content), [
            {'movie_id': 1, 'total_comments': 3, 'rank': 1},
            {'movie_id': 2, 'total_comments': 2, 'rank': 2},
            {'movie_id': 3, 'total_comments': 2, 'rank': 2}
        ])
