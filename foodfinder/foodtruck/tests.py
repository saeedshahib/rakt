from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from foodtruck.models import FoodTruck


class FoodTruckViewTests(TestCase):
    def setUp(self):
        FoodTruck.objects.all().delete()
        self.url = reverse('nearby-food-trucks')
        self.trucks_list = [
            {
                "name": "Truck 1",
                "facility_type": "",
                "address": "",
                "latitude": "0.00000000",
                "longitude": "0.00000000"
            },
            {
                "name": "Truck 2",
                "facility_type": "",
                "address": "",
                "latitude": "5.00000000",
                "longitude": "5.00000000"
            },
            {
                "name": "Truck 3",
                "facility_type": "",
                "address": "",
                "latitude": "10.00000000",
                "longitude": "10.00000000"
            },
            {
                "name": "Truck 4",
                "facility_type": "",
                "address": "",
                "latitude": "15.00000000",
                "longitude": "15.00000000"
            },
            {
                "name": "Truck 5",
                "facility_type": "",
                "address": "",
                "latitude": "20.00000000",
                "longitude": "20.00000000"
            },
            {
                "name": "Truck 6",
                "facility_type": "",
                "address": "",
                "latitude": "25.00000000",
                "longitude": "25.00000000"
            },
            {
                "name": "Truck 7",
                "facility_type": "",
                "address": "",
                "latitude": "30.00000000",
                "longitude": "30.00000000"
            },
            {
                "name": "Truck 8",
                "facility_type": "",
                "address": "",
                "latitude": "35.00000000",
                "longitude": "35.00000000"
            },
            {
                "name": "Truck 9",
                "facility_type": "",
                "address": "",
                "latitude": "40.00000000",
                "longitude": "40.00000000"
            },
            {
                "name": "Truck 10",
                "facility_type": "",
                "address": "",
                "latitude": "45.00000000",
                "longitude": "45.00000000"
            }
        ]
        for truck in self.trucks_list:
            FoodTruck.objects.create(
                name=truck['name'],
                latitude=truck['latitude'],
                longitude=truck['longitude']
            )

    def test_first_5_trucks(self):
        response = self.client.get(self.url, {'latitude': '0', 'longitude': '0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(response.json(), self.trucks_list[:5])

    def test_last_5_trucks(self):
        response = self.client.get(self.url, {'latitude': '100', 'longitude': '100'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(sorted(response.json(), key=lambda d: d['name']),
                         sorted(self.trucks_list[-5:], key=lambda d: d['name']))

    def test_mid_5_trucks(self):
        response = self.client.get(self.url, {'latitude': '20', 'longitude': '20'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(sorted(response.json(), key=lambda d: d['name']),
                         sorted(self.trucks_list[2:7], key=lambda d: d['name']))
