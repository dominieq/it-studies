import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def plot_kursy(kurs, a=None, b=None, c=None):
	plt.plot(kurs, 'r--', label="Dane")
	if None not in [a,b,c]:
		pred = np.zeros(len(kurs)-2)
		for i in range(2, len(kurs)):
		    pred[i-2] = a*kurs[i-1] + b*kurs[i-2] + c
		plt.plot(list(range(2,len(kurs))),pred, 'b:', label="Regresja")
	plt.legend()
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


def plot_reg(dane, a=None, b=None):
	x = dane['x']
	y = dane['y']
	plt.scatter(x,y, label="Dane")
	if None not in [a,b]:
		f = lambda x: a*x + b
		plt.plot(x,f(x),'k-', label="Regresja")
	plt.legend()
	plt.show()

def show_reconstructed_image(R, G, B):
    # Zmienne z problemu optymalizacyjnego przemieńmy na zwykłą macierz numpy.
    # Ponadto jest to problem optymalizacji ciągłej, a wartości pikseli są dyskretne! Wykonamy ucięcie do int'a
    assert R.size == G.size and R.size == B.size
    colors = 3
    rec_arr = np.zeros((R.size[1], R.size[0], colors), dtype=np.uint8)
    variables = [R, G, B]
    for i in range(colors):
        rec_arr[:, :, i] = variables[i].T.value

    img_rec = Image.fromarray(rec_arr)
    plt.imshow(img_rec);	
    plt.show()
