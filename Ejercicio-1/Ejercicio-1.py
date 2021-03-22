import matplotlib
import matplotlib.pyplot as plt

import skimage.filters
from skimage import io
import os


image = io.imread(os.getcwd() + '/Ejercicio-1/Img/ruido01.jpg', as_gray=False)
image2 = io.imread(os.getcwd() + '/Ejercicio-1/Img/Ejercicio1-a.jpg', as_gray=True)

# filteredImage = skimage.filters.gaussian(image, multichannel=False, sigma=2)

fig, ax = plt.subplots(1, 1)
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.hist(image.ravel(), bins=256, histtype='step', color='black', density=True)
ax1.set_title('Histograma Original')

fig2, ax2 = plt.subplots(1, 1)
ax2.imshow(image2, cmap=plt.cm.gray)
ax2.set_title('Prueba')
ax2.axis('off')

fig3, ax3 = plt.subplots(1, 1)
ax3.hist(image2.ravel(), bins=256, histtype='step', color='black', density=True)
ax3.set_title('Histograma De Prueba')

plt.show()