from unittest import TestCase

from src.utils.distances import nearest_pos, positions_sorted_by_distance

x1 = [0, 0, 0]
x2 = [2, 2, 3]
x3 = [200, 10 ** 4, -4567]
nb1 = [[1, 1, 1], [2, 2, 2]]
nb2 = [[0, 100, 0]]


class Test(TestCase):

    def test_nearest_point1(self):
        self.assertEqual(nb1[0], nearest_pos(x1, nb1))

    def test_nearest_point2(self):
        self.assertEqual(nb1[1], nearest_pos(x2, nb1))

    def test_nearest_point3(self):
        self.assertEqual(nb2[0], nearest_pos(x3, nb2))
