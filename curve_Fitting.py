from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from numpy import linspace
from random import random

t = linspace(0, 10, 500)
y = []

for x in t:
	var = 2*pow(x, 2) + 70*(random() * random())
	y.append(var)

def f(x, a, b):
	return b* pow(x, a)

var1 = curve_fit(f, t, y)
x1 = var1[0][0]
x2 = var1[0][1]
fit = []

for x in t:
	fit.append(f(x, x1, x2))


plt.plot(t, y)
plt.plot(t, fit)
plt.show()
