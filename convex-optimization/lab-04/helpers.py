from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from JSAnimation import IPython_display
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import sklearn.datasets as ds



# functions for animation
def init():
    line.set_data([], [])
    return line,

def animate(i):
    theta = history[i].reshape((-1,1))
    line.set_data(X_train[:, 0], np.dot(X_train_bias, theta))
    return line,

def animate_regression(X_train, y_train, history):
    theta = history[-1]
    best_fit_gradient_descent = theta[0] + X_train[:,0] * theta[1]
    fig = plt.figure(figsize=(10,6))
    ax = plt.axes(xlim=(-3, 3), ylim=(-10, 20))
    ax.plot(X_train[:,0], y_train, 'o')
    line, = ax.plot([], [], lw=2)
    plt.plot(X_train[:,0], best_fit_gradient_descent, 'k-', color = "r")
    animation.FuncAnimation(fig, animate, init_func=init,
                            frames=len(history), interval=100)

def plot_3d_linear_regression(X_train, y_train, cost_function, history=None):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.gca(projection='3d')
    #plt.hold(True)
    a = np.arange(1, 9, 0.25)
    b = np.arange(1, 9, 0.25)
    a, b = np.meshgrid(a, b) # make a grid of values from a and b
    # we use some vectorization to speed up the calculations
    c = [cost_function(X_train, y_train, [i, j]) for i, j in zip(a.ravel(), b.ravel())]
    c = np.array(c).reshape(a.shape)
    surf = ax.plot_surface(a, b, c, rstride=1, cstride=1, alpha=0.1, 
                           linewidth=0, antialiased=False)
    #ax.set_zlim(-0.01, 180.01)
    if history is not None:
        t0 = np.array([x[0] for x in history])
        t1 = np.array([x[1] for x in history])
        costs = [cost_function(X_train, y_train, [a, b]).reshape(a.shape) for a, b in zip(t0.ravel(), t1.ravel())]
        ax.scatter(t0, t1, costs, color="k"); 
    plt.show()

def plot_reg(X, y, beta=None):
	plt.scatter(X[:,-1],y, label="Dane")
	if beta is not None:
		f = lambda X: X@beta
		plt.plot(X[:,1],f(X),'k-', label="Regresja")
	plt.legend()
	plt.show()

def generate_data():
    X_train,y_train = ds.make_regression(n_samples=100, 
                                         n_features=1, 
                                         n_informative=1, 
                                         noise=20.0, 
                                         bias=50, 
                                         random_state=2016)
    y_train = y_train/10 # scale target to have nicer pictures

    plot_reg(X_train,y_train)
    return X_train,y_train


import time
def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap


def plot_algorithm_stats(historical_data, cost_function, slr = True):
    X = historical_data['X']
    y = historical_data['y']
    solutions = historical_data['solutions']

    if slr:
        cost_function = lambda x, y, beta: np.sum((np.dot(X, beta) - y) ** 2)
    costs = [cost_function(X, y, i) for i in solutions]
    final_solution = historical_data['final_solution']
    
    if slr:
	    beta_opt = np.linalg.inv(X.T@X)@X.T@y
	    optimal_cost = cost_function(X, y, beta_opt)
    solution_cost = cost_function(X, y, final_solution)
    
    
    print("Funkcja celu rozwiązania: ", solution_cost)
    if min(costs) != solution_cost:
        print(" (w czasie optymalizacji było jednak lepsze rozwiązanie z wartością {1})"\
              .format(solution_cost, min(costs)))
    if slr:
	    print("Optimum globalne: ", optimal_cost)
	    print('Względna różnica z optimum globalnym', (solution_cost- optimal_cost)/optimal_cost*100, '[%]')
	    print('Odległość od optimum globalnego',  np.linalg.norm(beta_opt-final_solution))
    
    plt.figure(figsize=(15,10))
    plt.subplot(2, 2, 1)
    plt.title("Funkcja celu ")
    plt.plot(np.arange(len(costs)), costs, label = 'funkcja kosztu rozwiązania')
    
    plt.subplot(2, 2, 2)
    start = int(len(costs)/2)
    plt.title("Funkcji celu (zoom końcówki)")
    plt.plot(np.arange(start, len(costs)),costs[start:], label = 'funkcja kosztu rozwiązania')
    if slr:
         plt.axhline(y=optimal_cost, color='r', linestyle='--', label = 'optimum globalne')
    plt.legend()
    
    plt.subplot(2, 2, 4)
    eta_history = historical_data['eta_history']
    plt.title("Prędkość optymalizacji w kolejnych iteracjach")
    plt.plot(np.arange(len(eta_history)), eta_history)
    
    plt.subplot(2, 2, 3)
    gradients = historical_data['gradients']
    updates = [np.linalg.norm(i*j) for i,j in zip(gradients, eta_history)]
    update_scale = [i/np.linalg.norm(j) for i,j in zip(updates,solutions)]
    plt.title("Względny rozmiar aktualizacji")
    plt.axhline(y=0.001, color='grey', linestyle='--', label = '10**-3')
    plt.plot(np.arange(len(update_scale)),update_scale)
    plt.show()


def plot_classification(x, y, labels, a=None, b=None, c=None):
	if None not in [a,b,c]:
		delta = 0.025
		x_vals = np.arange(min(x), max(x), delta)
		y_vals = np.arange(min(y), max(y), delta)
		X, Y = np.meshgrid(x_vals,y_vals)
		Z = a*X+b*Y+c		
		CS = plt.contour(X, Y, Z, 6, colors='k')
		plt.clabel(CS, fontsize=9, inline=1)
	plt.scatter(x, y, c = labels)
	plt.show()
