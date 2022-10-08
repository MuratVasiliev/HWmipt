import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def blur(img_arr, weights_arr):
    img_arr = img_arr.astype('float')
    img_arr /= 255
    weights_arr /= weights_arr.sum()
    if len(img_arr.shape) == 3:
        r = scipy.signal.convolve2d(img_arr[:,:,0], weights_arr, mode='same')
        g = scipy.signal.convolve2d(img_arr[:,:,1], weights_arr, mode='same')
        b = scipy.signal.convolve2d(img_arr[:,:,2], weights_arr, mode='same')
        a = np.dstack([r, g, b])
        a[a > 255] = 255
        a = (a*255).astype('uint8')
        return a
    else:
        r = scipy.signal.convolve2d(img_arr[:,:], weights_arr, mode='same')
        g = scipy.signal.convolve2d(img_arr[:,:], weights_arr, mode='same')
        b = scipy.signal.convolve2d(img_arr[:,:], weights_arr, mode='same')
        a  = np.dstack([r, g, b])
        a[a > 255] = 255
        a= (a*255).astype('uint8')
        return a

img = Image.open('osa.jpeg')
img_arr = np.array(img)
w = 1 - np.abs(np.linspace(-1,1,31))
weights_arr = w.reshape(31,1)*w.reshape(1,31)

fig, ax = plt.subplots(2, figsize=(10,10))
ax[0].imshow(img)
ax[1].imshow(blur(img_arr, weights_arr))
plt.show()