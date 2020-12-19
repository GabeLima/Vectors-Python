from unittest import TestCase
from two_d_point import TwoDPoint


class TestTwoDPoint(TestCase):

    def test_from_coordinates(self):
        t = TwoDPoint
        potential = t.from_coordinates([-5, 4, 3, 4, 3, 0, 0, 0])
        actual = [TwoDPoint(-5, 4), TwoDPoint(3, 4), TwoDPoint(3, 0), TwoDPoint(0, 0)]
        self.assertEqual(potential, actual)

    def test_eq(self):
        self.assertEqual(TwoDPoint(4, 0), TwoDPoint(4, 0))

    def test_ne(self):
        self.assertNotEqual(TwoDPoint(0, 0), TwoDPoint(5, 0))

    def test_str(self):
        self.assertEqual(TwoDPoint.__str__(TwoDPoint(0, 4)), "(0, 4)")

    def test_add(self):
        self.assertEqual(TwoDPoint(5, 0) + TwoDPoint(0, 5), TwoDPoint(5, 5))

    def test_sub(self):
        self.assertEqual(TwoDPoint(5, 3) - TwoDPoint(4, 4), TwoDPoint(1, -1))

