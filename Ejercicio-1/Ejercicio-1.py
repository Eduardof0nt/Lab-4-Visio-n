import matplotlib
import matplotlib.pyplot as plt

import skimage.filters
from skimage import io
import os

filename = os.getcwd() + '/Ejercicio-1/Img/Ejercicio1-b.jpeg'

image = io.imread(filename, as_gray=True)
imageOriginal = io.imread(filename, as_gray=False)

# thresh = skimage.filters.threshold_otsu(image)
# binary = image > thresh

fig, ax = plt.subplots(1, 1)
ax.imshow(imageOriginal, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

# ax[0].imshow(imageOriginal, cmap=plt.cm.gray)
# ax[0].set_title('Original')
# ax[0].axis('off')

# ax[1].imshow(binary, cmap=plt.cm.gray)
# ax[1].set_title('Thresholded')
# ax[1].axis('off')

fig1, ax1 = skimage.filters.try_all_threshold(image, figsize=(10, 6), verbose=False)

plt.show()