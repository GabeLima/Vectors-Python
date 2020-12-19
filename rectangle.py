from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint


class Rectangle(Quadrilateral):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

    def __is_member(self):
        side_lengths = self.side_lengths()
        return side_lengths[0] == side_lengths[2] and side_lengths[1] == side_lengths[3]

    def center(self):
        temp_center = self.vertices[0] + self.vertices[1] + self.vertices[2] + self.vertices[3]
        return TwoDPoint(temp_center.x/4.0, temp_center.y/4.0)

    def area(self):
        side_lengths = self.side_lengths()
        return side_lengths[0] * side_lengths[1]

    def __eq__(self, other):
        super().__eq__(other)

    def __str__(self):
        super(self)
