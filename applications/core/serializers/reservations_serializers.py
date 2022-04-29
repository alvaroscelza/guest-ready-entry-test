from rest_framework import serializers

from applications.core.models import Reservation


class ReservationsWithPreviousSerializer(serializers.ModelSerializer):
    rental_name = serializers.SerializerMethodField()
    previous_reservation = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['rental_name', 'id', 'checkin', 'checkout', 'previous_reservation']

    @staticmethod
    def get_rental_name(reservation):
        return reservation.rental.name

    def get_previous_reservation(self, reservation):
        reservations_with_same_rental = self.Meta.model.objects.filter(rental=reservation.rental)
        all_previous = reservations_with_same_rental.filter(checkout__lte=reservation.checkin)
        return self.get_latest_previous_pk(all_previous)

    @staticmethod
    def get_latest_previous_pk(all_previous):
        """Returns the latest element 'pk' based on the 'checkout' date field. Returns '-' if list is empty."""
        if all_previous:
            return all_previous.latest('checkout').pk
        return '-'
