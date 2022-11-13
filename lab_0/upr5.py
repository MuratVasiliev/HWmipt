import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y = x[::-1].reshape((-1, 1))
dist = x**2+(y+1-abs(x)**0.5)-1
img = dist
plt.imshow(img)
plt.show()