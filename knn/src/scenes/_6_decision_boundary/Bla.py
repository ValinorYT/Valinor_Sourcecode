import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from general.data.dots.dots1 import positions, labels_3_classes
from general.data.graphics_stuff import LABEL_COLORS


def plot_decision_boundaries(x, y, model):
    grid_resolution = .01
    x, y = np.array(x), np.array(y).flatten()
    xx, yy = np.meshgrid(np.arange(x[:, 0].min() - 1, x[:, 0].max() + 1, grid_resolution),
                         np.arange(x[:, 1].min() - 1, x[:, 1].max() + 1, grid_resolution))

    model.fit(x, y)
    z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.contourf(xx, yy, z, alpha=0.4, colours=LABEL_COLORS)

    print(z)
    print(type(z))

    plt.scatter(x[:, 0], x[:, 1], c=[LABEL_COLORS[labels_3_classes[i]] for i in range(len(positions))], s=130)
    return plt


plt.figure()
plot_decision_boundaries(positions, labels_3_classes, KNeighborsClassifier(n_neighbors=15))
plt.show()
