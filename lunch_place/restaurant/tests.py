from django.test import TestCase
from restaurant.models import Restaurant, Menu
from app_logging import logger
from datetime import date


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


class MenuTestCase(TestCase):

    description = "Test Description"
    menu_date = date.today()

    def test_menu_create(self):
        logger.info(
            "Menu Create Test Running"
        )
        restaurant = Restaurant.objects.create(
            name='Test',
            address='Test',
            rating=3.5
        )
        restaurant.save()
        Menu.objects.create(
            restaurant_id=restaurant,
            description=self.description,
            menu_date=self.menu_date
        )
        res = Menu.objects.all()
        self.assertGreater(len(res), 0)
