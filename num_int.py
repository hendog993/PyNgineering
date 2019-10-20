# Import statements
from matplotlib import pyplot as plt
from scipy.integrate import trapz, simps, cumtrapz
from math import sin, cos, pi, log, exp
from random import random
from numpy import linspace

t = linspace(0.001, 2*pi, 1000)
y = []

def integrate(lim_a, lim_b):
	func = lambda x: x * log(x) - x
	return func(lim_b) - func(lim_a)
	
	
for x in t:
	var = 3*pow(x, 3) + 100*(random() * random())
	y.append(var)
	
area_trapz = trapz(y, t)
area_simps = simps(y, t)
print("Area trapezoidal rule: {}".format(area_trapz))
print("Area Simpson's Rule: {}" .format(area_simps))
# print("Area FTC1: {}".format(integrate(0.001, 2*pi)))

plt.plot(t, y)
plt.show()
