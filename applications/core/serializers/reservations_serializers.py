from rest_framework import serializers

from applications.core.models import Reservation


class ReservationReadSerializer(serializers.ModelSerializer):
    rental_name = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['rental_name', 'id', 'checkin', 'checkout']

    @staticmethod
    def get_rental_name(reservation):
        return reservation.rental.name
