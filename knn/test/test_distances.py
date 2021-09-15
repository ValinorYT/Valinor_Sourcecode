from unittest import TestCase

from manim import Dot

from knn.src.utils.distances import stuff_sorted_by_distance

x1 = Dot([0, 0, 0])
x2 = Dot([2, 2, 3])
x3 = Dot([200, 10 ** 4, -4567])
nb1 = [Dot([1, 1, 1]), Dot([2, 2, 2])]
nb2 = [Dot([0, 100, 0])]


class Test(TestCase):

    def test_nearest_point1(self):
        self.assertEqual(nb1[0], stuff_sorted_by_distance(x1, nb1)[0])

    def test_nearest_point2(self):
        self.assertEqual(nb1[1], stuff_sorted_by_distance(x2, nb1)[0])

    def test_nearest_point3(self):
        self.assertEqual(nb2[0], stuff_sorted_by_distance(x3, nb2)[0])
