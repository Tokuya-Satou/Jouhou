import matplotlib.pyplot as plt
import random

kosu = 1000

x = [0]
y=[0]

for i in range(kosu):
    if random.random() < 0.5:
        ido = 1
    else:
        ido = -1
    
    x.append(x[i]+0.1)
    y.append(y[i]+ido)

plt.plot(x,y)
plt.show
