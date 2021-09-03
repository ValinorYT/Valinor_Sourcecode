import numpy as np


def nearest_pos(x, nb):
    distances = np.linalg.norm(np.array(x) - np.array(nb), axis=1)
    return nb[distances.argmin()]


# Not stable yet
def positions_sorted_by_distance(x, nb):
    distances = np.linalg.norm(np.array(x) - np.array(nb), axis=1)
    sorted_indices = distances.argsort()
    return np.array(nb)[sorted_indices]


# Used for quick testing right now
x1 = [0, 0, 0]
x2 = [2, 2, 3]
x3 = [200, 10 ** 4, -4567]
nb1 = [[1, 1, 1], [2, 2, 2]]
nb2 = [[0, 100, 0]]

if __name__ == '__main__':
    x = positions_sorted_by_distance(x1, nb1)
    print(x)
