import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import skimage.filters
from skimage import io
import os

filename = os.getcwd() + '/Ejercicio-2/Img/Ejercicio2-a.jpg'

grey_scale=False

image = io.imread(filename, as_gray=grey_scale)

count = 0

filtered_img = image.copy();

if(not grey_scale):
    filtered_img[filtered_img <= 215] = 0;
    filtered_img[(filtered_img > 215) & (filtered_img < 250)] = 128;
    filtered_img[filtered_img >= 250] = 255;
else:
    filtered_img[filtered_img <= 0.8] = 0;
    filtered_img[(filtered_img > 0.8) & (filtered_img < 0.96)] = 0.5;
    filtered_img[filtered_img >= 0.96] = 1;

fig, ax = plt.subplots(1, 1)
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.hist(image.ravel(), bins=256, histtype='step', color='black', density=True)
ax1.set_title('Histograma Original')

fig2, ax2 = plt.subplots(1, 1)
ax2.imshow(filtered_img, cmap=plt.cm.gray)
ax2.set_title('Filtrada')
ax2.axis('off')

fig3, ax3 = plt.subplots(1, 1)
ax3.hist(filtered_img.ravel(), bins=256, histtype='step', color='black', density=True)
ax3.set_title('Histograma Filtrado')

plt.show()