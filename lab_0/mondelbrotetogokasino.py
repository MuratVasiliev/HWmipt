import matplotlib.pyplot as plt
import numpy as np

re = np.linspace(-2, 2, 200)
im = np.linspace(-2, 2, 200).reshape((-1, 1))
c = re + im * 1j

z = np.zeros((200, 200))
for i in range(100):
    z = z ** 2 + c

img = np.zeros((200, 200))
img[np.abs(z) < 2] = 255
plt.imshow(img)
plt.show()
