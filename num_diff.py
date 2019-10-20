from numpy import linspace, gradient
from matplotlib import pyplot as plt
from math import sin, pi, cos

t = linspace(0, 2*pi, 1000)
y = []

for x in t:
	# Input your function here.
	var = sin(x)
	y.append(var)

dy = gradient(y)
dt = gradient(t)
dydt = dy/dt

plt.plot(t,y, label='Function')
plt.grid()
plt.plot(t, dydt, label="Derivative")
plt.xlabel(" t (radians)")
plt.ylabel(" Sin(t)")
plt.legend()
plt.show()

