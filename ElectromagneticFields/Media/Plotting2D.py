import matplotlib.pyplot as plt
import numpy as np
import math as m

f = lambda x, y: (x/(x**2+y**2), y/(x**2+y**2))
r = 10
X, Y = np.meshgrid(range(-r, r + 1), range(-r, r + 1)) # the Sample of the Domain

Xhat, Yhat = f(X, Y)

W, graph = plt.subplots()

graph.quiver(X, Y, Xhat, Yhat, scale=15)
plt.savefig("ElectromagneticFields/Media/Graphs/Point.png")
plt.show()