from django.urls import path

from foodtruck.views import NearbyFoodTruckView, food_truck_list

urlpatterns = [
    path('find_nearby/', NearbyFoodTruckView.as_view(), name='nearby-food-trucks'),  # Restful
    path('food_trucks/', food_truck_list, name='food_truck_list'),  # Template render
]
