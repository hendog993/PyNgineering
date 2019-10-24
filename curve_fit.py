from numpy import linspace, log, sin, pi
from matplotlib import pyplot as plt
from random import random
from scipy.optimize import curve_fit

t = linspace(0.001, 5, 100)
y = []

for i in t:
	var = 2*log(i) + 8 * (random() * random())
	y.append(var)

# Linear equation: y = ax+b
def logarithmic(x, a, b):
	return a*log(x) + b

constants = curve_fit(logarithmic, t, y)
a_fit = constants[0][0]
b_fit = constants[0][1]

fit = []
for i in t:
	fit.append(logarithmic(i, a_fit, b_fit))


plt.plot(t, y)
plt.plot(t, fit)
plt.grid()
plt.xlabel("t")
plt.ylabel("y")
plt.title("Python Curve Fit")
plt.show()
