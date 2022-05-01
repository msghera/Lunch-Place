from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from restaurant.models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from rest_framework import permissions


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(
        restaurants,
        many=True
    )
    return Response(serializer.data)


@api_view(['POST'])
def add_restaurant(request):
    serializer = RestaurantSerializer(
        data = request.data
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else : 
        return Response(serializer.errors, 400)



## Get one restaurant
## Update restaurant

@api_view(['GET'])
def get_menus(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(
        menus,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def add_menu(request):
    serializer = MenuSerializer(
        data = request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else : 
        return Response(serializer.errors, 400)