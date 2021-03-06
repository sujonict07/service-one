import unittest
from ....app_manager.utils import string_reverser


class TestBasic(unittest.TestCase):

    def setUp(self):
        self.input_string = "iPay"
        self.reverse_string = self.input_string[::-1]

    def test_reverse_string(self):
        payload = {"message": self.input_string}
        reverse_string = string_reverser(payload)
        self.assertEqual(self.reverse_string, reverse_string)
