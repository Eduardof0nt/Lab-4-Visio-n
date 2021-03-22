import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import math

from skimage import data
from skimage.filters import try_all_threshold

from skimage import io
import os

import scipy.ndimage

filename = os.getcwd() + '/Ejercicio-3/Img/ruido03.png'

img = io.imread(filename, as_gray=False)

Gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Gy = np.rot90(Gx, k=1)

G45 = np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
G135 = np.rot90(G45, k=1)
print(G45)
print(G135)

def convolve_1d(array, kernel):
    ks = kernel.shape[0] # shape gives the dimensions of an array, as a tuple
    final_length = array.shape[0] - ks + 1
    return np.array([(array[i:i+ks]*kernel).sum() for i in range(final_length)])

def convolve_2d(array,kernel):
    ks = kernel.shape[1] # shape gives the dimensions of an array, as a tuple
    final_height = array.shape[1] - ks + 1
    return np.array([convolve_1d(array[:,i:i+ks],kernel) for i in range(final_height)]).T


image1 = convolve_2d(img, Gx)
image2 = convolve_2d(img, Gy)
image3 = convolve_2d(img, G45)
image4 = convolve_2d(img, G135)

image5 = image1*0
for i in range(0,image1.shape[0]):
    for j in range(0,image1.shape[1]):
        image5[i,j] = (image1[i,j]**2 + image2[i,j]**2)**0.5


fig, ax = plt.subplots(1, 1)
ax.imshow(img, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.imshow(image1, cmap=plt.cm.gray)
ax1.set_title('Convolución horizontal')
ax1.axis('off')

fig2, ax2 = plt.subplots(1, 1)
ax2.imshow(image2, cmap=plt.cm.gray)
ax2.set_title('Convolución vertical')
ax2.axis('off')

fig3, ax3 = plt.subplots(1, 1)
ax3.imshow(image3, cmap=plt.cm.gray)
ax3.set_title('Convolución 45º')
ax3.axis('off')

fig4, ax4 = plt.subplots(1, 1)
ax4.imshow(image4, cmap=plt.cm.gray)
ax4.set_title('Convolución 135º')
ax4.axis('off')

fig5, ax5 = plt.subplots(1, 1)
ax5.imshow(image5, cmap=plt.cm.gray)
ax5.set_title('Convolución Total')
ax5.axis('off')

plt.show()