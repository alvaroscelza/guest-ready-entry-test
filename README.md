# <<Project Name>>

<<Project description.>>

## Technology Stack

-   Python 3.9.1
-   Django 4

## Installation and running

### Without Docker

-   Create virtual environment and activate it. Example: `virtualenv venv`
-   Enter environment: Example: `venv\Scripts\activate`
-   Install requirements:
    -   Development: `pip install -r requirements/development.txt`
    -   Production: `pip install -r requirements/base.txt`
-   `pre-commit install`
-   Create an .env file at project root for storing secrets. File .env-example is provided as a guide of this file's content. Make sure you copy your SECRET_KEY there.
-   `python manage.py makemigrations`
-   `python manage.py migrate`
-   `python manage.py createsuperuser`
-   Run using `python manage.py runserver`

### With Docker

-   Create `docker-compose.yml` (you may use docker-compose.example.yml as reference)
-   Make sure to have Docker running on your system (in mac, you should have docker icon in top menu).
-   Run using: `docker-compose up`

## Testing

### Without Docker

-   Run the tests with `python manage.py test`
-   Get test coverage with `coverage run --source='.' manage.py test` and then `coverage report --skip-covered --show-missing`

### With Docker

-   Make sure your service name for the django app is `web` or change it accordingly in the following commands.
-   Run the tests with `docker-compose run web python manage.py test`
-   Get test coverage with:
    -   `docker-compose run web coverage run --source='.' manage.py test`
    -   `docker-compose run web coverage run --source='.' manage.py test`
