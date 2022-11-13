from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
w, h = 1920,1080
img = Image.new("RGB", (w, h), "white")
img_arr = img.load()
x0, y0 = -1, 0

for x in range(w):
    for y in range(h):
        zx = 1.5*(x - w/2)/(0.5*w)
        zy = 1.0*(y - h/2)/(0.5*h)
        i = 255
        while zx**2 + zy**2 < 4 and i > 1:
            fixed_x = zx**2 - zy**2 + x0
            zy, zx = 2.0*zx*zy + y0, fixed_x
            i -= 1
            img_arr[x,y] = (i << 21) + (i << 10) + i*8
plt.imshow(img)
plt.show()