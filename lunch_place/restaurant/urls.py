from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_restaurants),
    path('add/', views.add_restaurant),

    path('menu/', views.get_menus),
    path('menu/add/', views.add_menu),
]
