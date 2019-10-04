import unittest
import random
from ....app_manager.utils import random_number_generator


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.random_number = random.random()

    def test_random_number_generator(self):
        random_number = random_number_generator(10, chars='123')
        self.assertNotEqual(self.random_number, random_number)
