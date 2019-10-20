# Numerical Differentiation 
from matplotlib import pyplot as plt
from math import sin, cos, pi
from numpy import gradient, linspace

t = linspace(0, 2*pi, 1000)
y = []

# This is the function input
for x in t:
	var = sin(x) * cos(x)
	y.append(var)

dy = gradient(y)
dt = gradient(t)
dydt = dy/dt

plt.plot(t,y, label="Function")
plt.grid()
plt.plot(t, dydt, label="Derivative")
plt.xlabel("t (radians)")
plt.ylabel("y")
plt.legend()
plt.show()
