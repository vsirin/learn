import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-150, -75]
A = [[10, 4], [3, 2], [2, 5]]
b = [1000, 360, 600]

res = linprog(c, A, b)
print(res)


plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()

plt.xlabel("x")
plt.xlim(0, 200)
plt.ylabel("y")
#plt.ylim(-800, 800);

x = np.linspace(0, 200, 1000)

l1 = ax.plot(x, (1000 - 10*x)/4, color='blue', label='10x+4y=1000')
l2 = ax.plot(x, (360 - 3*x)/2, color='red', label='3x+2y=360')
l3 = ax.plot(x, (600 - 2*x)/5, color='green', label='2x+5y=600')
l4 = ax.plot(res.x[0], res.x[1], marker="x")
ax.text(2, 6, "150x+75y->max\nx>=0\ny>=0\n10x+4y<=1000\n3x+2y<=360\n2x+5y<=600\n")

ax.legend()
plt.show()


