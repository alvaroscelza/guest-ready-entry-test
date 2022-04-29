from django.contrib import admin

from applications.core.models import Rental, Reservation

admin.site.register(Rental)
admin.site.register(Reservation)
