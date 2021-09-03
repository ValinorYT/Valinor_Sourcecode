import numpy as np


def nearest_pos(x, nb):
    distances = np.linalg.norm(np.array(x) - np.array(nb), axis=1)
    return nb[distances.argmin()]
