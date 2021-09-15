import numpy as np


def stuff_sorted_by_distance(x, stuff):
    x_np = np.array(x.get_center())
    return sorted(stuff, key=lambda i: np.linalg.norm(x_np - np.array(i.get_center())))
