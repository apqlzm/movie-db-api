from typing import Dict, List, Optional, Tuple

from omdbapi.models import Movie, Rating
from datetime import datetime


RatingData = List[dict]
MovieData = Dict
MovieRatingData = Tuple[MovieData, List[dict]]


def _to_date(x: str) -> datetime:
    return datetime.strptime(x, '%d  %b %Y')


converters = {
    "Released": _to_date,
    "Runtime": lambda x: int(x.replace(' min', '')),
    "DVD": _to_date,
    "imdbVotes": lambda x: x.replace(',', '')
}


def find_movie_in_db(title: str) -> Optional[Movie]:
    movie = Movie.objects.filter(title__iexact=title)
    if movie:
        return movie[0]
    return None


def _parse_movie_data(movie_data: dict) -> MovieRatingData:
    """Parse movie data obtained from omdbapi

    - match data to application's model
    - omit unneeded data fields (example: "Response")
    - skip fields with "N/A" values

    Returns:
        Tuple with movie and rating dictionaries
    """
    IGNORED_KEYS = ('response', 'ratings', 'type')
    parsed_movie_data = {}

    for key, v in movie_data.items():
        if v == 'N/A':
            continue

        key_lower = key.lower()

        if key_lower not in IGNORED_KEYS:
            converter = converters.get(key)
            parsed_movie_data[key_lower] = converter(v) if converter else v

    parsed_movie_data['type_picture'] = movie_data['Type']

    ratings = movie_data['Ratings']
    parsed_rating_data = []

    for rating in ratings:
        parsed_rating_data.append(
            {
                'source': rating['Source'],
                'value': rating['Value']
            }
        )

    return parsed_movie_data, parsed_rating_data


def create_new_movie(movie_data: dict) -> Movie:
    """Create movie and associated ratings
    """
    movie_data, rating_data = _parse_movie_data(movie_data)
    movie = Movie(**movie_data)
    movie.save()

    for rating in rating_data:
        movie.ratings.create(**rating)

    return movie

def get_all_movies():
    return Movie.objects.all()