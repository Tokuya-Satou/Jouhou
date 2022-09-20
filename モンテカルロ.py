import matplotlib.pyplot as plt
import random, math
import numpy as np

kosu = 1000

x = []
y = []
r = []
r_num = 0

for i in range(kosu):
    x.append(random.random())
    y.append(random.random())
    r.append(math.sqrt(x[i]**2+y[i]**2))
    if r[i] <= 1:
        r_num = r_num +1

print(4*r_num/kosu)

t = np.linspace(0, np.pi/2, 100)

plt.scatter(x,y)
plt.plot(np.cos(t),np.sin(t))
plt.show()

