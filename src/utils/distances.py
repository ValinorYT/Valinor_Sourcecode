import numpy as np
from manim import Dot


def nearest_pos(x, nb):
    distances = np.linalg.norm(np.array(x) - np.array(nb), axis=1)
    return nb[distances.argmin()]


# Not stable yet
def dots_sorted_by_distance(x, nb):
    x_np = np.array(x.get_center())
    return sorted(nb, key=lambda i: np.linalg.norm(x_np - np.array(i.get_center())))


# Used for quick testing right now
x1 = Dot([0, 0, 0])
x2 = Dot([2, 2, 3])
x3 = Dot([200, 10 ** 4, -4567])
nb1 = [Dot([1, 1, 1]), Dot([2, 2, 2])]
nb2 = [Dot([0, 100, 0])]

if __name__ == '__main__':
    x = dots_sorted_by_distance(x1, nb1)
    print(x[0].get_center())
    print(x[1].get_center())
