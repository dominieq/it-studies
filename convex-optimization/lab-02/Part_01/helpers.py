import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import exp, sin, ceil, cos

plt.style.use("ggplot")


class Function(object):
    def __init__(self, func, dimensions=1, name="???"):
        self.name = name
        assert dimensions > 0
        self.dims = dimensions
        self._func = func

    def get_value(self, x):
        return self._func(x)

    def plot(self, start=-10, end=10, num=200, points=None, num_ticks=9):
        if self.dims not in [1, 2]:
            raise ValueError("Plotting not supported for dimensions > 2!")

        if self.dims == 1:
            X = np.linspace(start, end, num)
            Y = []
            for x in X:
                Y.append(self._func(x))

            plt.plot(X, Y)

            if points is not None:
                X = []
                Y = []
                for x in points:
                    X.append(x)
                    Y.append(self.get_value(x))

                plt.scatter(X, Y)

        elif self.dims == 2:
            if points is not None:
                points = np.array(points, dtype=np.float32)
                start = min(points.min(), start)
                end = max(end, points.max())
            cells = np.linspace(start, end, num)

            m = np.zeros((len(cells), len(cells)))
            for x_i, x in enumerate(cells):
                for y_i, y in enumerate(cells):
                    m[x_i, y_i] = self._func(np.array([x, y]))

            sns.heatmap(np.flip(m.T, 0))
            ticks = np.linspace(start, end, num_ticks)
            plt.xticks(np.linspace(0, len(cells), num_ticks), ticks, rotation='horizontal')
            plt.yticks(np.linspace(0, len(cells), num_ticks), np.flip(ticks, 0))

            if isinstance(points, np.ndarray):
                points[:, 1] *= -1
                points -= start
                points *= num / (end - start)
                plt.scatter(*points.T, color="b")

        if self.name is not None:
            plt.title(self.name)
        plt.show()


linear1d = Function(lambda x: 2 * x + 0.5, name="y = 2x +0.5", dimensions=1)
linear2d = Function(lambda x: 2 * x[1] + 3 * x[1] + 0.3, name="y = 2x0 + 3x1 + 0.3", dimensions=2)

functions_1d = [
    Function(lambda x: x ** 2, name="x^2", dimensions=1),
    Function(lambda x: x ** 3, name="x^3", dimensions=1),
    Function(lambda x: -x , name="-x", dimensions=1),
    Function(lambda x: abs(x), name="abs", dimensions=1),
    Function(lambda x: -exp(-x ** 2), name="gauss", dimensions=1),
    Function(lambda x: sin(x), name="sine wave", dimensions=1),
Function(lambda x: x**2 +sin(x), name="sine wave with a twist", dimensions=1),
    Function(lambda x: ceil(abs(x)), name="steps", dimensions=1),
]

functions_2d = [
    Function(lambda x: sum(x**2), name="circle", dimensions=2),
    Function(lambda x: x[0]**2 - x[1]**2, name="saddle", dimensions=2),
    Function(lambda x: sum(-np.exp(-(x-5)**2/10)), name="gauss", dimensions=2),
    Function(lambda x: -0.06*sum(abs(x-3)**1.7)+(sin(x[0] + 2*cos(x[1]) + sin(x[0]*sin(x[1])))), name="LSD", dimensions=2),
    Function(lambda x: sum(np.ceil(abs(x/2))), name="steps", dimensions=2),
]

easy_100d_func = Function(lambda x: 100+sum(-np.exp(-(x-8)**2*10)), name="easy", dimensions=100)
