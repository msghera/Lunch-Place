from dataclasses import field
from genericpath import exists
from rest_framework .serializers import ModelSerializer, ValidationError
from restaurant.models import Restaurant, Menu

import datetime

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, data):
        is_exist = Menu.objects.filter(
            restaurant_id = data['restaurant_id'],
            menu_date = datetime.date.today()
        ).exists()
        if is_exist:
            raise ValidationError('Menu already exists for today.')

        return Menu(**data)