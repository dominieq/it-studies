import copy
from angrybirds.abAPI import *
from angrybirds.helpers import plot_history, play_action

"""
Do wykonania tego zadania konieczna jest instalacja:

pip3 install --user pymunk pygame

Prawdopodobnie znasz grę AngryBirds. W tym zadaniu będziemy starali nauczyć się (zoptymalizować)
kąt pod jakim należy wystrzelić naszego bird'a aby trafić w zwierzątko i wygrać grę. 
Twoim zadaniem będzie napisać algorytm spadku wzdłuż gradientu oraz wymyślić (i zaimplementować)
funkcję celu, której optymalizacja pozwoli na wygranie gry ;)
* Prawdziwy problem jest trochę bardziej skomplikowany (wymaga też ustawienia siły rzutu), ale 
aby pozostac w problemie 1D siłę rzutu ustawiono na pewną stałą.

Twoje zadania:
- cost_function - zaimplementuj obliczanie funkcji celu (możesz wykorzystać pomocniczą funkcję distance)
- gradient_descent - zaimplementuj algorytm Gradient Descent (używając oczywiście cost_function)
"""

evaluation_history = {}
#Stała do wykorzystania w algorytmie
epsilon = 0.001

def distance(point1, point2):
	"""distance between points"""
	dx = point1[0] - point2[0]
	dy = point1[1] - point2[1]
	return ((dx ** 2) + (dy ** 2)) ** 0.5


def cost_function(x, game):
	state, path, _ = play_action(game, x) #Wykonaj rzut
	"""
	- state zawiera słownik state.pigs['positions'] zawierający listę par (x,y) z pozycjami zwierzątek do zbicia
	- path zawiera listę par (x,y) będącymi kolejnymi pozycjami lecącego ptaka (rysowane jako biała krzywa)
	"""
	# Twój kod tutaj
	cost = None



	evaluation_history[x] = cost #Zapis ewaluacji do narysowania wykresu
	return cost 

def gradient_descent(cost_function):
	x = 2.05  # Punkt startowy
	eta = 0.000003 # Stała regulująca szybkość optymalizacji
	for i in range(50): #Wykonaj maksymalnie 50 iteracji optymalizacji
		# TWÓJ KOD TUTAJ 
		derivative = 0
		

		cost = cost_function(x)
		print("Iter {0}: x={1}\tpochodna={2}\tf. celu={3}".format(i, x, derivative, cost))
		if abs(derivative) < epsilon :  #warunek stopu - zerowa pochodna 
			# (de facto funkcja nie jest wypukła więc to niekoniecznie musi być minimum :/
			print ("Znalezeiono minimum!")
			break
	return x


if __name__ == "__main__":
	game = AngryBirdsMDP() # Start gry
	gradient_descent(lambda x : cost_function(x, game)) #Optymalizacja
	plot_history(evaluation_history) #Narysuj wykres funkcji
