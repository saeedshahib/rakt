from rest_framework import serializers
from foodtruck.models import FoodTruck


class FoodTruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodTruck
        fields = ["name", "facility_type", "address", "latitude", "longitude"]
