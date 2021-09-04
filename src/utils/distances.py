import numpy as np


def dots_sorted_by_distance(x, my_dots):
    x_np = np.array(x.get_center())
    return sorted(my_dots, key=lambda i: np.linalg.norm(x_np - np.array(i.get_center())))
