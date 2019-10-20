from matplotlib import pyplot as plt
from math import sin, cos, pi, exp, log
from scipy.integrate import simps, trapz, cumtrapz
from numpy import linspace
from random import random

# Function for true integral
def integrate(lim_a, lim_b):
	func = lambda x: (1/2)*exp(2*x)
	return func(lim_b) - func(lim_a)


t = linspace(0.1, 2*pi, 1000)
y = []
y_area = 0

for x in t:
	var = exp(2*x)
	y.append(var)

area_traps = trapz(y, t)
area_simps = simps(y, t)

print(area_traps)
print(area_simps)
print(integrate(0.1, 2*pi))
plt.plot(t, y)
plt.grid()
plt.show()
