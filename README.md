# Touch Grass API

This project uses Django

Ensure you have python and pip installed

## Pipenv

### `python -m pip install pipenv`

Installs pipenv on your computer

### `python -m pipenv shell`

Activates the project virtual enviroment

### `pipenv install --dev`

Install project dependencies outlined in Pipfile

### `exit`

Exit the virtual enviroment

## Development

Navigate to the `/touchgrass` directory within api

### `python manage.py createsuperuser`

Create a super user

### `python manage.py migrate`

Migrate database table updates to the server

### `python manage.py runserver`

Start up the development server

### Open `localhost:8000` on your browser
