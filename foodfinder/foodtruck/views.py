from decimal import Decimal

from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import render

from foodtruck.models import FoodTruck
from foodtruck.serializers import FoodTruckSerializer


# Restful Api
class NearbyFoodTruckView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = FoodTruck.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            latitude = Decimal(str((request.GET['latitude'])))
            longitude = Decimal(str((request.GET['longitude'])))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid or missing latitude/longitude parameters'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            nearby_food_trucks = FoodTruck.find_nearby_trucks(latitude=latitude, longitude=longitude)
            serializer = FoodTruckSerializer(nearby_food_trucks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ve:
            return Response({'error': 'server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# interface
def food_truck_list(request):
    context = {}
    if 'latitude' in request.GET and 'longitude' in request.GET:
        try:
            latitude = Decimal(str((request.GET['latitude'])))
            longitude = Decimal(str((request.GET['longitude'])))
            context['food_trucks'] = FoodTruck.find_nearby_trucks(latitude, longitude)
        except (ValueError, TypeError):
            context['error'] = 'Invalid or missing latitude/longitude parameters'

    return render(request, 'foodfinder.html', context)
