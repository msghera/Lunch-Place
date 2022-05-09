from django.test import TestCase
from restaurant.models import Restaurant
from app_logging import logger


class RestaurantTestCase(TestCase):

    name = "Test Name"
    address = "Test Address"
    rating = 4.0

    def test_restaturant_create(self):
        logger.info(
            "Restaurant Create Test Running"
        )
        Restaurant.objects.create(
            name=self.name,
            address=self.address,
            rating=self.rating
        )
        res = Restaurant.objects.filter(
            name=self.name
        )
        self.assertGreater(len(res), 0)

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')