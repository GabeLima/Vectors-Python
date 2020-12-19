import math

from two_d_point import TwoDPoint


class Quadrilateral:

    def __init__(self, *floats):
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])

    @property
    def vertices(self):
        return self.__vertices

    def side_lengths(self):
        first_length = self.__vertices[0] - self.__vertices[1]
        first_length = math.sqrt(first_length.x * first_length.x + first_length.y * first_length.y)
        second_length = self.__vertices[1] - self.__vertices[2]
        second_length = math.sqrt(second_length.x * second_length.x + second_length.y * second_length.y)
        third_length = self.__vertices[2] - self.__vertices[3]
        third_length = math.sqrt(third_length.x * third_length.x + third_length.y * third_length.y)
        fourth_length = self.__vertices[0] - self.__vertices[3]
        fourth_length = math.sqrt(fourth_length.x * fourth_length.x + fourth_length.y * fourth_length.y)
        return first_length, second_length, third_length, fourth_length

    def smallest_x(self):
        x0 = self.__vertices[0].x
        x1 = self.__vertices[1].x
        x2 = self.__vertices[2].x
        x3 = self.__vertices[3].x
        min_x = min(x0, x1)
        min_x = min(min_x, x2)
        min_x = min(min_x, x3)
        return min_x

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            temp_self = self.__vertices
            temp_other = other.__vertices
            return temp_self[0] == temp_other[0] and temp_self[1] == temp_other[1] and temp_self[2] == temp_other[2] \
                   and temp_self[3] == temp_other[3]

    def __str__(self):
        return "Type of instance: %s, Smallest x of instance:%g" % (type(self), self.smallest_x())
