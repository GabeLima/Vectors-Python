from unittest import TestCase
from rectangle import Rectangle
from two_d_point import TwoDPoint


class TestRectangle(TestCase):

    def test_center(self):
        test_rectangle = Rectangle(0, 4, 3, 4, 3, 0, 0, 0).center()
        center = TwoDPoint(1.5, 2)
        self.assertEqual(test_rectangle, center)

    def test_area(self):
        test_rectangle = Rectangle(0, 4, 3, 4, 3, 0, 0, 0).area()
        area = 12
        self.assertEqual(test_rectangle, area)
        area = 27
        self.assertNotEqual(test_rectangle, area)
