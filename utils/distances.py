import itertools

import numpy as np


def nearest_neighbour(x, nb):
    distances = [np.linalg.norm(np.array(a) - np.array(b)) for a, b in zip(itertools.cycle(x), nb)]
    return np.argmin(distances)
