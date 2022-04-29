import datetime

import factory
from factory.django import DjangoModelFactory

from applications.core.models import Reservation
from applications.core.tests.factories.rentals_factory import RentalsFactory


class ReservationsFactory(DjangoModelFactory):
    class Meta:
        model = Reservation

    rental = factory.SubFactory(RentalsFactory)
    checkin = datetime.datetime.now()
    checkout = datetime.datetime.now() + datetime.timedelta(days=10)
