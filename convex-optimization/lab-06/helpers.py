import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import exp, sin, ceil, cos
#from input_data import read_data_sets
from scipy.optimize import linesearch
import warnings
from random import random

plt.style.use("ggplot")

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")


def plot_gd_1d(function, x_in_time, axis_range = None):
    x_in_time = np.array(x_in_time)
    y_in_time = np.array([function(x) for x in x_in_time])
    points_span = max(x_in_time) - min(x_in_time)
    margin = 0.5
    grid_points = 100
    if axis_range is None:
        x_left = min(x_in_time) - margin * points_span
        x_right = max(x_in_time) + margin * points_span
    else:
        x_left, x_right = axis_range
    x_grid = np.linspace(x_left, x_right, grid_points)
    y_grid = np.array([function(x) for x in x_grid[:, np.newaxis]])

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6.15))

    error_in_time_plot = ax[0]
    gradients_plot = ax[1]

    # Plot arrows for gradients:
    for ti in range(1, len(x_in_time)):
        # Determine start of an arrow
        x, y = x_in_time[ti], function(x_in_time[ti])
        # Determine end of an arrow
        old_x, old_y = x_in_time[ti - 1], function(x_in_time[ti - 1])
        # Plot a red arrow
        gradients_plot.annotate('', xy=(x, y),
                                xytext=(old_x, old_y),
                                arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 2},
                                va='center', ha='center')

    # Plot points themselves:
    gradients_plot.scatter(x_in_time[[0, -1]], y_in_time[[0, -1]], c="blue", s=70, lw=0)
    gradients_plot.scatter(x_in_time[1:-1], y_in_time[1:-1], c="magenta", s=50, lw=0)
    gradients_plot.plot(x_grid, y_grid, 'k')
    gradients_plot.set_xlim(x_left, x_right)
    gradients_plot.set_ylabel('f(x)')
    gradients_plot.set_xlabel('x')
    gradients_plot.set_title('')

    error_in_time_plot.set_title("error in time")
    error_in_time_plot.set_ylabel('f(x)')
    error_in_time_plot.set_xlabel('iterations')

    error_in_time_plot.plot(y_in_time)
    plt.tight_layout()


def plot_gd_2d(function, x_in_time, contours = False, axis_range = None):
    x_in_time = np.array(x_in_time, dtype=np.float64)
    y_in_time = np.array([function(x) for x in x_in_time])

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6.15))
    error_in_time_plot = ax[0]
    gradients_plot = ax[1]

    margin = 1
    grid_points = 1000
    num_ticks = 5
    x0_span = abs(x_in_time[:, 0].max() - x_in_time[:, 0].min())
    x1_span = abs(x_in_time[:, 1].max() - x_in_time[:, 1].min())
    x0_axis_min_lim = x_in_time[:, 0].min() - margin * x0_span
    x0_axis_max_lim = x_in_time[:, 0].max() + margin * x0_span
    x1_axis_min_lim = x_in_time[:, 1].min() - margin * x1_span
    x1_axis_max_lim = x_in_time[:, 1].max() + margin * x1_span

    if axis_range is None:
        min_lim = min(x0_axis_min_lim, x1_axis_min_lim)
        max_lim = max(x0_axis_max_lim, x1_axis_max_lim)
    else:
        min_lim, max_lim = axis_range
    lim_span = max_lim - min_lim

    x0_grid = np.linspace(min_lim, max_lim, grid_points)
    x1_grid = np.linspace(min_lim, max_lim, grid_points)

    m = np.zeros((grid_points, grid_points))
    for x0_i, x in enumerate(x0_grid):
        for x1_i, y in enumerate(x1_grid):
            m[x0_i, x1_i] = function(np.array([x, y]))

    x0_ticks = np.linspace(min_lim, max_lim, num_ticks)
    x1_ticks = np.linspace(min_lim, max_lim, num_ticks)
    x0_ticks = ["{:0.2f}".format(x0) for x0 in x0_ticks]
    x1_ticks = ["{:0.2f}".format(x1) for x1 in x1_ticks]

    x_in_time -= min_lim
    x_in_time /= lim_span
    x_in_time[:, 1] = 1-x_in_time[:, 1]
    x_in_time *= grid_points

    # Plot arrows for gradients:
    for ti in range(1, len(x_in_time)):
        # Determine start of an arrow
        x, y = x_in_time[ti]
        # Determine end of an arrow
        old_x, old_y = x_in_time[ti - 1]
        # Plot a red arrow
        gradients_plot.annotate('', xy=(x, y),
                                xytext=(old_x, old_y),
                                arrowprops={'arrowstyle': '->', 'color': 'pink', 'lw': 2},
                                va='center', ha='center')
    if contours:
        CS = gradients_plot.contour(np.flip(m.T, 0))
        gradients_plot.clabel(CS, inline=1, fontsize=10)
    else:
        sns.heatmap(np.flip(m.T, 0), ax=gradients_plot)
    gradients_plot.scatter(*x_in_time[[0, -1]].T, c="white", s=70, lw=0)
    gradients_plot.scatter(*x_in_time[1:-1].T,  c="magenta", s=50, lw=0)

    gradients_plot.set_xticks(np.linspace(0, grid_points, num_ticks))
    gradients_plot.set_xticklabels(x0_ticks)
    gradients_plot.set_yticks(np.linspace( grid_points,0, num_ticks))
    gradients_plot.set_yticklabels(x1_ticks)
    gradients_plot.tick_params(axis='x', rotation=0)

    error_in_time_plot.set_title("error in time")
    error_in_time_plot.set_ylabel('f(x)')
    error_in_time_plot.set_xlabel('iterations')

    error_in_time_plot.plot(y_in_time)
    plt.axis('equal')
    plt.tight_layout()



def aprroximate_line_search(f, gradient, x, direction):
    g = gradient(x)
    alpha_k, fc, gc, old_fval, old_old_fval, gfkp1 = line_search_wolfe12(f, gradient, x, direction, g, f(x), \
                                                                             f(x) + np.linalg.norm(g) / 2,\
                                                                             amin=1e-100, amax=1e100)
    return alpha_k
            
            
class LineSearchError(RuntimeError):
    pass

def line_search_wolfe12(f, fprime, xk, pk, gfk, old_fval, old_old_fval,
                         **kwargs):
    """
    Same as line_search_wolfe1, but fall back to line_search_wolfe2 if
    suitable step length is not found, and raise an exception if a
    suitable step length is not found.
    Raises
    ------
    _LineSearchError
        If no suitable step size is found
    """

    extra_condition = kwargs.pop('extra_condition', None)

    ret = linesearch.line_search_wolfe1(f, fprime, xk, pk, gfk,
                             old_fval, old_old_fval,
                             **kwargs)

    if ret[0] is not None and extra_condition is not None:
        xp1 = xk + ret[0] * pk
        if not extra_condition(ret[0], xp1, ret[3], ret[5]):
            # Reject step if extra_condition fails
            ret = (None,)

    if ret[0] is None:
        # line search failed: try different one.
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', linesearch.LineSearchWarning)
            kwargs2 = {}
            for key in ('c1', 'c2', 'amax'):
                if key in kwargs:
                    kwargs2[key] = kwargs[key]
            ret = linesearch.line_search_wolfe2(f, fprime, xk, pk, gfk,
                                     old_fval, old_old_fval,
                                     extra_condition=extra_condition,
                                     **kwargs2)

    if ret[0] is None:
        raise LineSearchError()

    return ret
