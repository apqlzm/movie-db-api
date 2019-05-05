# Movie API

## Short description

Api fetches movie data from *www.omdbapi.com* and saves it to database.

## Requirements

Api was developed using **Django** and **Django REST** frameworks. Additionally **requests** library was used to interact with *www.omdbapi.com* api. Database on production server is Postgresql (instead of sqlite which was used only for development) so psycopg2 database adapter was added to requirements file.

Api tested with Python 3.7

## How to run project locally

Clone repository and got to project's root directory afterwards follow steps:

1. Activate python virtual environment <br />
`source /path/to/local/env`

2. Install requirements <br />
`pip install -r requirements.txt`

3. Run server <br />
`python manage.py runserver`

4. Api can be tested by sending requests to address `http://127.0.0.1:8000/resource_name`

## Endpoints

### GET /movies/

Download all movies.

### POST /movies/

Download movie data from external api and save it in database.

Required Headers: <br />
Content-Type: application/json

Required json body fields: <br />
title

### DELETE /movies/<movie-id>/

Delete movie

movie-id from URL is used to determine which movie should be deleted

### UPDATE /movies/<movie_id>/

Update movie

Required Headers: <br />
Content-Type: application/json

Json body should contain field names and values which supposed to be updated. For instance:

```json
{
    "title": "Terminator",
    "year": "1993",
    "rated": "",
    "released": "2019-01-02",
    "runtime": 39,
    "genre": "Short, Action, Sci-Fi",
    "director": "Ben Hernandez",
}
```

movie-id from URL is used to determine which movie should be updated

### POST /comments

Create comment attached to movie

Required Headers: <br />
Content-Type: application/json

Json body requires body and movie_id fields.

```json
{
    "body": "Good movie",
    "movie_id": 1
}
```

### GET /comments

Show all created comments or only comments attached to specific movie

To get comments attached to specific movie add query params so that url will look like `comments/?movie_id=1`

### GET /top

Show movie ranking based on number of comments

Required query params **date_from**, **date_to**

## Demo

Api deployed to **https://movie-db-api.cleverapps.io**