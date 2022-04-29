from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from applications.core.tests.factories.rentals_factory import RentalsFactory
from applications.core.tests.factories.reservations_factory import ReservationsFactory


class ReservationsTestCase(APITestCase):
    def setUp(self):
        self.reservations_url = reverse('reservations-list')

    def test_get_reservations_with_previous_ok_no_reservations(self):
        response = self.client.get(self.reservations_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_get_reservations_with_previous_ok_one_reservation(self):
        reservation = ReservationsFactory.create()

        response = self.client.get(self.reservations_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['rental_name'], reservation.rental.name)
        self.assertEqual(response.data['results'][0]['id'], reservation.pk)
        self.assertEqual(response.data['results'][0]['checkin'], reservation.checkin.strftime('%Y-%m-%d'))
        self.assertEqual(response.data['results'][0]['checkout'], reservation.checkout.strftime('%Y-%m-%d'))
        self.assertEqual(response.data['results'][0]['previous_reservation'], '-')

    def test_get_reservations_with_previous_ok_multiple(self):
        """This test replicates the test data given on the email."""
        rental_1 = RentalsFactory.create(name='Rental-1')
        reservation_1 = ReservationsFactory.create(rental=rental_1, checkin='2022-01-01', checkout='2022-01-13')
        reservation_2 = ReservationsFactory.create(rental=rental_1, checkin='2022-01-20', checkout='2022-02-10')
        reservation_3 = ReservationsFactory.create(rental=rental_1, checkin='2022-02-20', checkout='2022-03-10')
        rental_2 = RentalsFactory.create(name='Rental-2')
        reservation_4 = ReservationsFactory.create(rental=rental_2, checkin='2022-01-02', checkout='2022-01-20')
        reservation_5 = ReservationsFactory.create(rental=rental_2, checkin='2022-01-20', checkout='2022-02-11')

        response = self.client.get(self.reservations_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 5)
        self.assertEqual(response.data['results'][0]['rental_name'], rental_1.name)
        self.assertEqual(response.data['results'][0]['id'], reservation_1.pk)
        self.assertEqual(response.data['results'][0]['checkin'], reservation_1.checkin)
        self.assertEqual(response.data['results'][0]['checkout'], reservation_1.checkout)
        self.assertEqual(response.data['results'][0]['previous_reservation'], '-')
        self.assertEqual(response.data['results'][1]['rental_name'], rental_1.name)
        self.assertEqual(response.data['results'][1]['id'], reservation_2.pk)
        self.assertEqual(response.data['results'][1]['checkin'], reservation_2.checkin)
        self.assertEqual(response.data['results'][1]['checkout'], reservation_2.checkout)
        self.assertEqual(response.data['results'][1]['previous_reservation'], reservation_1.pk)
        self.assertEqual(response.data['results'][2]['rental_name'], rental_1.name)
        self.assertEqual(response.data['results'][2]['id'], reservation_3.pk)
        self.assertEqual(response.data['results'][2]['checkin'], reservation_3.checkin)
        self.assertEqual(response.data['results'][2]['checkout'], reservation_3.checkout)
        self.assertEqual(response.data['results'][2]['previous_reservation'], reservation_2.pk)
        self.assertEqual(response.data['results'][3]['rental_name'], rental_2.name)
        self.assertEqual(response.data['results'][3]['id'], reservation_4.pk)
        self.assertEqual(response.data['results'][3]['checkin'], reservation_4.checkin)
        self.assertEqual(response.data['results'][3]['checkout'], reservation_4.checkout)
        self.assertEqual(response.data['results'][3]['previous_reservation'], '-')
        self.assertEqual(response.data['results'][4]['rental_name'], rental_2.name)
        self.assertEqual(response.data['results'][4]['id'], reservation_5.pk)
        self.assertEqual(response.data['results'][4]['checkin'], reservation_5.checkin)
        self.assertEqual(response.data['results'][4]['checkout'], reservation_5.checkout)
        self.assertEqual(response.data['results'][4]['previous_reservation'], reservation_4.pk)
