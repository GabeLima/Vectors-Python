from quadrilateral import Quadrilateral


class ShapeSorter(Quadrilateral):

    @staticmethod
    def sort(*args: Quadrilateral):
        new_list = []
        for x in args:
            new_list.append(x)
        n = len(new_list)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if new_list[j].smallest_x() > new_list[j + 1].smallest_x():
                    new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

        return new_list
