# Movie API

## Short description

Api fetches movie data from  

## Requirements

Api was developed using **Django** and **Django REST** frameworks. Additionally **requests** library was used to interact with *www.omdbapi.com* api. Database on production server is Postgresql (instead of sqlite which was used only for development) so psycopg2 database adapter was added to requirements file.

Api tested with Python 3.7

## How to run locally

Clone repository and got to project's root directory afterwards follow steps:

1. Activate python virtual environment <br />
`source /path/to/local/env`

2. Install requirements <br />
`pip install -r requirements.txt`

3. Run server <br />
`python manage.py runserver`

4. Api can be tested by sending requests to address `http://127.0.0.1:8000/resource_name`

## Demo

Api deployed to **https://movie-db-api.cleverapps.io**