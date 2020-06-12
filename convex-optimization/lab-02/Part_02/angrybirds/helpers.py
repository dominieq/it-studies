import copy
from .abAPI import *
from .GameAgent import angryAgent
import matplotlib.pyplot as plt


def plot_history(evaluation_history):
    x = []
    y = []
    for i, j in evaluation_history.items():		
        x.append(i)
        y.append(j)
    plt.scatter(x,y)
    plt.title('Historia ewaluacji')
    plt.show()

def distance(point1, point2):
    """distance between points"""
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return ((dx ** 2) + (dy ** 2)) ** 0.5


def play_action(mdp, x, maxIterations=1, verbose=True, show = True):

    output = {}
    if show: mdp.showLearning()

    state = mdp.startState()
    if verbose: mdp.showState()

    for k in range(maxIterations):
         newState,reward, path = mdp.succAndReward(state, (x, 70))

         if newState==None:
             break
         if verbose: mdp.showState()
         state = newState
    
    return state, path, reward


