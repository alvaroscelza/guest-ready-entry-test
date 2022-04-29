# GuestReady Entry Test

- Below you will find instructions on techs used, how to run locally (with venv), how to run with docker and how to run
tests. I've also provided example templates, though they only contain dummy data.
- Django Admin has also been enabled and has the two models registered, to simplify manual testing.
- You will also find a complete project structure, thought to include internationalization, different managers for the
models ORM, serializers (using Django REST Framework), diagrams documentation (using PUML), static content (for
when the project includes a frontend), templatetags (functions callable from the frontend templates), test coverage,
flake8, pre-commit hooks and docker.
- All requirements are set in the requirements.txt file. They are not pinned, though that's recommended on a real
project.
- It's also prepared to host many applications to modularize the entire project.
- I didn't use Gitflow because I'm the only developer, and it's a small project, but I use it on all my actual projects.
- The ReadableWritableModelView is a custom view Mixin I use to build Views that should behave differently when reading
from them than when writing to them. It also includes authentication permission. We don't need it in this project, but I
left it as example.
- The architecture of this project includes patterns such as MVC (which is implemented by Django), REST (implemented
using DRF) and Layers of Isolation.
- Settings are separated into 3 files: a base file containing common settings, a development and a production files to
hold each environment's specific settings.
- The ReservationsView inherits from DRF's ModelViewSet and thus, it provides full CRUD operations. Those operations
won't work since the serializer I use was created specifically for the operation that was requested. Other serializers
should be created for other endpoints, but I left them to show the full productivity potential of DRF. It also has the line
`# permission_classes = [IsAuthenticated]` commented as an example, but we won't use authentication to simplify.
- I've implemented Swagger and you can use it to access and test the API at http://<domain>/api/v1/swagger/.
- The endpoint that returns "the table of Reservations with previous reservation ID." is at
`/reservations/get_reservations_with_previous/`
- Pagination is also implemented.

Have fun :)

## Assumptions
- All Reservations have "correct" dates. That means: checkout date is always greater than, or equals its checkin date.
This could be checked with custom validations: https://docs.djangoproject.com/en/4.0/ref/forms/validation/
- Reservations don't overlap for a same rental. Otherwise, the logic for get_previous_reservation in the serializer
would be more complex.
- Performance is not an issue: as you may notice, each time we call the endpoint get_reservations_with_previous, a call
to database is done to fetch all reservations (because of calling `all()`), and then another call is made in
get_previous_reservation to filter the prev reservation.

## Effort Registry

The entire project took 108 minutes to be completed.

## Technology Stack

-   Python 3.10.3
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
