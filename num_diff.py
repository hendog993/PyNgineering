import numpy as np
from matplotlib import pyplot as plt
from math import sin, pi
t = []
y = []

# Sin function goes from 0-180
t = np.linspace(0,2*pi, 1000)


for x in t:
	y.append(sin(x))

dy = np.gradient(y)
dx = np.gradient(t)
dydx =dy/dx


plt.plot(t, y)
plt.plot(t, dydx)
plt.show()
