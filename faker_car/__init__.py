from faker.providers import BaseProvider
from .enums import CARS

class CarProvider(BaseProvider):

    def car(self):
        return self.car_brand()

    def car_brand(self):
        return self.random_element(elements=CARS.keys())

    def car_model(self):
        brand = self.car_brand()
        model = self.random_element(elements=CARS.get(brand))
        return brand, model



