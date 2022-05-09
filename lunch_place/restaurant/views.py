from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from restaurant.models import Restaurant, Menu
from .serializers import (
    RestaurantSerializer,
    MenuSerializer
)
from rest_framework import permissions

from app_logging import logger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import (
    Schema,
    TYPE_OBJECT,
    TYPE_NUMBER,
    TYPE_STRING,
)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(
        restaurants,
        many=True
    )
    logger.info('Returning all the restaurants')
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=Schema(
    type=TYPE_OBJECT,
    properties={
        'name': Schema(type=TYPE_STRING, description='Restaurant Name'),
        'address': Schema(type=TYPE_STRING, description='Restaurant Address'),
        'rating': Schema(type=TYPE_NUMBER, description='Restaurant Rating'),
    }
))
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def add_restaurant(request):
    serializer = RestaurantSerializer(
        data=request.data
    )
    if serializer.is_valid():
        logger.info('Creating a new restaurants')
        serializer.save()
        return Response(serializer.data)
    else:
        logger.error('Error in creating restaurant.')
        return Response(serializer.errors, 400)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_menus(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(
        menus,
        many=True
    )

    logger.info('Returning all the Menus (for anyday).')
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=Schema(
    type=TYPE_OBJECT,
    properties={
        'restaurant_id': Schema(type=TYPE_NUMBER, description='Restaurant ID'),
        'description': Schema(
            type=TYPE_STRING,
            description='Menu Description'
        ),
    }
))
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def add_menu(request):
    serializer = MenuSerializer(
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        logger.info('Adding a new menu for today.')
        return Response(serializer.data)
    else:
        logger.error('Error in creating new menu.')
        return Response(serializer.errors, 400)
