from django.apps import AppConfig


class FoodtruckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodtruck'

    def ready(self):
        from foodtruck.models import FoodTruck
        try:
            FoodTruck.import_food_truck_data()
        except:
            pass
