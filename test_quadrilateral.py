from unittest import TestCase

from rectangle import Rectangle
from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint


class TestQuadrilateral(TestCase):

    def test_side_lengths(self):
        quad_length_1 = Quadrilateral(0, 4, 3, 4, 3, 0, 0, 0).side_lengths()
        quad_length_2 = Quadrilateral(3, 4, 6, 4, 6, 0, 3, 0).side_lengths()
        self.assertEqual(quad_length_1, quad_length_2)
        quad_length_2 = Quadrilateral(3, 4, 5, 4, 5, 0, 3, 0).side_lengths()
        self.assertNotEqual(quad_length_1, quad_length_2)

    def test_smallest_x(self):
        quad_small_1 = Quadrilateral(0, 4, 3, 4, 3, 0, -6, 0).smallest_x()
        quad_small_2 = Quadrilateral(-6, 4, 3, 4, 3, 0, 0, 0).smallest_x()
        self.assertEqual(quad_small_1, quad_small_2)

    def test_eq(self):
        quad_small_1 = Quadrilateral(0, 4, 3, 4, 3, 0, -6, 0)
        quad_small_2 = Quadrilateral(0, 4, 3, 4, 3, 0, -6, 0)
        self.assertEqual(quad_small_1, quad_small_2)
        quad_small_1 = Rectangle(0, 4, 3, 4, 3, 0, 0, 0)
        quad_small_2 = Quadrilateral(0, 4, 3, 4, 3, 0, -6, 0)
        self.assertNotEqual(quad_small_1, quad_small_2)

    def test_str(self):
        self.assertEqual(Quadrilateral.__str__(Quadrilateral(0, 4, 3, 4, 3, 0, -6, 0)), "Type of instance: <class "
                                                                                        "'quadrilateral.Quadrilateral"
                                                                                        "'>, Smallest x of "
                                                                                        "instance:-6")
