from rest_framework.test import APITestCase

from applications.core.tests.factories.rentals_factory import RentalsFactory


class UniqueNameMixinsTests(APITestCase):
    def test_to_string_ok(self):
        some_unique_name_object = RentalsFactory.build()

        object_to_string = some_unique_name_object.__str__()

        self.assertEqual(object_to_string, some_unique_name_object.name)
