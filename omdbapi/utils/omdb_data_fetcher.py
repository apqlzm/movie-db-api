import requests
from django.conf import settings

OMDB_URL = 'http://www.omdbapi.com/'


def get_movie_data(title: str) -> dict:
    """Download movie data with given title
    """
    if not title:
        return {}

    api_key = settings.OMDB_API_KEY
    payload = {
        'apikey': api_key,
        't': title
    }
    r = requests.get(url=OMDB_URL, params=payload)

    if r.status_code == 200:
        data_dict = r.json()
        if data_dict['Response'] == 'True':
            return data_dict
    return {}
