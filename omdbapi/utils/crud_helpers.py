from collections import Counter
from datetime import date, datetime
from typing import Dict, List, Optional, Tuple, Union

from omdbapi.models import Comment, Movie, Rating

RatingData = List[dict]
MovieData = Dict
MovieRatingData = Tuple[MovieData, List[dict]]


def _to_date(x: str) -> date:
    return datetime.strptime(x, '%d  %b %Y').date()


converters = {
    "Released": _to_date,
    "Runtime": lambda x: int(x.replace(' min', '')),
    "DVD": _to_date,
    "imdbVotes": lambda x: x.replace(',', '')
}


def find_movie_in_db(title: str) -> Optional[Movie]:
    # TODO: doesnt work in some cases, example: "Good Bye Lenin!"
    # or "harry potter"
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


def create_new_movie(movie_data: dict) -> Optional[Movie]:
    """Create movie and associated ratings
    """
    if not movie_data:
        return None

    movie_data, rating_data = _parse_movie_data(movie_data)
    movie = Movie(**movie_data)
    movie.save()

    for rating in rating_data:
        movie.ratings.create(**rating)

    return movie


def get_all_movies():
    return Movie.objects.all()


def _serialize_top_list(counter: Counter) -> List[dict]:
    """Movie ranking based on counter data
    """
    output = []
    last_quantity = -1
    current_rank = 0

    for movie_id, quantity in counter.most_common():
        if last_quantity != quantity:
            last_quantity = quantity
            current_rank += 1

        output.append({
            'movie_id': movie_id,
            'total_comments': quantity,
            'rank': current_rank
        })

    return output


def prepare_top_list(date_from: datetime, date_to: datetime) -> List[dict]:
    comments = Comment.objects.filter(
        date_created__date__gte=date_from.date()
    ).filter(
        date_created__date__lte=date_to.date()
    )
    counter = Counter([c.movie_id for c in comments])
    return _serialize_top_list(counter)
