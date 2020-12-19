from unittest import TestCase
from two_d_point import TwoDPoint
from square import Square
from quadrilateral import Quadrilateral


class TestSquare(TestCase):

    def test_snap(self):
        snapped_square = Square(0.1, 4.1, 4.1, 4.1, 4.1, 0.1, 0.1, 0.1).snap()
        expected_snap = Quadrilateral(0, 4, 4, 4, 4, 0, 0, 0)
        self.assertEqual(snapped_square, expected_snap)
        snapped_square = Square(0.1, .4, .5, .4, .5, 0, 0.1, 0).snap()
        expected_snap = Square(0.1, .4, .5, .4, .5, 0, 0.1, 0)
        self.assertEqual(snapped_square.vertices, expected_snap.vertices)
