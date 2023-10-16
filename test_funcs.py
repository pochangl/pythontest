from unittest import TestCase
from funcs import add


class TestAdd(TestCase):
    def test_1_plus_1(self):
        self.assertEqual(add(1, 1), 2)

    def test_1_plus_2(self):
        self.assertEqual(add(1, 2), 2)