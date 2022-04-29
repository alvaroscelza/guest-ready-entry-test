import factory
from factory.django import DjangoModelFactory

from applications.core.models import Rental


class RentalsFactory(DjangoModelFactory):
    class Meta:
        model = Rental

    name = factory.Faker('pystr')
