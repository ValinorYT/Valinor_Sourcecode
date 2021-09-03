from unittest import TestCase

from utils.distances import nearest_pos


class Test(TestCase):
    x1 = [0, 0, 0]
    x2 = [2, 2, 3]
    x3 = [200, 10 ** 4, -4567]
    nb1 = [[1, 1, 1], [2, 2, 2]]
    nb2 = [[0, 100, 0]]

    def test_nearest_point1(self):
        self.assertEqual(self.nb1[0], nearest_pos(self.x1, self.nb1))

    def test_nearest_point2(self):
        self.assertEqual(self.nb1[1], nearest_pos(self.x2, self.nb1))

    def test_nearest_point3(self):
        self.assertEqual(self.nb2[0], nearest_pos(self.x3, self.nb2))
