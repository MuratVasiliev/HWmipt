def gaussian_blur(img_array, sigma, w_size):
    gauss_array = np.zeros((w_size, w_size))
    for x in range(-w_size // 2, w_size // 2 + 1):
            for y in range(-w_size // 2, w_size // 2 + 1):
                d = np.sqrt(x ** 2 + y ** 2)
                gauss_array[x + w_size // 2][y + w_size // 2] = 1/(2*np.pi*sigma**2)*np.exp(-d**2/(2*sigma**2))
    img_blurred = blur(img_array, gauss_array)
    return img_blurred
plt.imshow(gaussian_blur(img_array, 15, 31))