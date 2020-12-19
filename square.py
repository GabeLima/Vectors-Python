from two_d_point import TwoDPoint
from rectangle import Rectangle
from quadrilateral import Quadrilateral


class Square(Rectangle):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    def snap(self):
        vertices = self.vertices
        if round(vertices[0].x) == round(vertices[2].x):
            return self
        elif round(vertices[0].y) == round(vertices[2].y):
            return self
        else:
            # vertices[0] = TwoDPoint(round(vertices[0].x), round(vertices[0].y))
            # vertices[1] = TwoDPoint(round(vertices[1].x), round(vertices[1].y))
            # vertices[2] = TwoDPoint(round(vertices[2].x), round(vertices[2].y))
            # vertices[3] = TwoDPoint(round(vertices[3].x), round(vertices[3].y))
            temp = Quadrilateral(round(vertices[0].x), round(vertices[0].y), round(vertices[1].x),
                                 round(vertices[1].y), round(vertices[2].x), round(vertices[2].y),
                                 round(vertices[3].x), round(vertices[3].y))
            return temp

    def __eq__(self, other):
        super().__eq__(other)

    def __str__(self):
        super(self)

    def __is_member(self):
        lengths = self.side_lengths()
        return lengths[0] == lengths[1] == lengths[2] == lengths[3]
