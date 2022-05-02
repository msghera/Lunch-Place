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

    def validate(self, attr):
        is_exist = Menu.objects.filter(
            restaurant_id=attr['restaurant_id'],
            menu_date=datetime.date.today()
        ).exists()
        if is_exist:
            raise ValidationError('Menu already exists for today.')

        return attr
