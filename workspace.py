from matplotlib import pyplot as plt
from numpy import linspace, array
from numpy.linalg import solve

t = linspace(-10, 0, 100)
y1 = []
y2 = []
y3 = []

f1 = lambda x: 3 * x + 5.43
f2 = lambda x: -.51 * x - 12
f3 = lambda x: 1.43 * x + 1.2
# -3x + y = 5.43    # eq 1
# .51x + y = - 12   # eq 2
# -1.43x + y = 1.2  # eq 3
for i in t:
	y1.append(f1(i))
	y2.append(f2(i))
	y3.append(f3(i))

# Intersections: 23, 21, 13
# Find solution to 2-3
a23 = array([[.51, 1], [-1.43, 1]])
b23 = array([-12, 1.2])
sol23 = solve(a23, b23)

# Find solution to 2-1
a21 = array([[.51, 1], [-3, 1]])
b21 = array([-12, 5.43])
sol21 = solve(a21, b21)

# Find solution to 13
a13 = array([[-3, 1], [-1.43, 1]])
b13 = array([5.43, 1.2])
sol13 = solve(a13, b13)

plt.plot(t, y1, label="Equation 1")
plt.plot(t, y2, label="Equation 2")
plt.plot(t, y3, label="Equation 3")
plt.grid()
plt.scatter(sol23[0], sol23[1], label="2-3 Solution")
plt.scatter(sol21[0], sol21[1], label="2-1 Solution")
plt.scatter(sol13[0], sol13[1], label="1-3 Solution")
plt.legend()
plt.title("Solving Linear Equations")
plt.xlabel(" x ")
plt.ylabel(" y ")
plt.show()
