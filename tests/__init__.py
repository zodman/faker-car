import unittest
from faker import Faker
from src import CarProvider



class TestCarProvider(unittest.TestCase):
    def setUp(self):
        self.fake = Faker('')
        Faker.seed(0)
        self.fake.add_provider(CarProvider)

    def test_car(self):
        assert self.fake.car()
        assert self.fake.car_model()
