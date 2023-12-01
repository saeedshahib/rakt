import csv
from decimal import Decimal
import math

from django.db import models
from django.db.models import F, ExpressionWrapper, Value, DecimalField
from django.db.models.functions import Power, Sqrt
from django.conf import settings

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FoodTruck(BaseModel):
    name = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=8, max_digits=32)
    longitude = models.DecimalField(decimal_places=8, max_digits=32)

    def __str__(self):
        return self.name

    @staticmethod
    def import_food_truck_data():
        with open(settings.CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                latitude = round(Decimal(str(row['Latitude'])), 8)
                longitude = round(Decimal(str(row['Longitude'])), 8)
                name = str(row['Applicant'])

                FoodTruck.objects.get_or_create(
                    name=name,
                    latitude=latitude,
                    longitude=longitude,
                    defaults={
                        "facility_type": row['FacilityType'],
                        "address": row['Address'],
                    }
                )

    @staticmethod
    def find_nearby_trucks(latitude, longitude, max_results=5):
        # Convert input to Decimal for precision in calculations
        latitude = Decimal(latitude)
        longitude = Decimal(longitude)

        # Calculate the square of the difference in latitudes and longitudes
        trucks = FoodTruck.objects.annotate(
            distance=ExpressionWrapper(
                Sqrt(Power(F('latitude') - latitude, 2) + Power(F('longitude') - longitude, 2)),
                output_field=DecimalField()
            )
        ).order_by('distance')

        # Order by 'distance' and limit the results to 'max_results'
        nearest_trucks = trucks[:max_results]

        return nearest_trucks
