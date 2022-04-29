from django.db import models

from applications.core.models.rental import Rental


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
