import matplotlib
import matplotlib.pyplot as plt

import skimage.filters
from skimage import io
import os

image1 = io.imread(os.getcwd() + '/Ejercicio-2/Img/ruido02.jpg', as_gray=False)

filteredImage1 = skimage.filters.gaussian(image1, multichannel=False, sigma=2)

fig, ax = plt.subplots(1, 1)
ax.imshow(image1, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.hist(image.ravel(), bins=256, histtype='step', color='black', density=True)
ax1.set_title('Histograma Original')

fig2, ax2 = plt.subplots(1, 1)
ax2.imshow(filteredImage1, cmap=plt.cm.gray)
ax2.set_title('Filtrada')
ax2.axis('off')

plt.show()