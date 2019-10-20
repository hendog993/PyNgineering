from matplotlib import pyplot as plt
from numpy import linspace
from math import log, pi, sin
from scipy.integrate import simps
from random import random

t = linspace(0.001, 2*pi, 1000)
y = []


for x in t:
	var = sin(x) + (random() * random())
	y.append(var)

area = simps(y, t)
print(area)


plt.plot(t, y)
plt.show()
