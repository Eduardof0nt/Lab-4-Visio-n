import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import skimage.filters
from skimage import io
import os

import math

filename = os.getcwd() + '/Ejercicio-4/Img/Ejercicio4-a.png'

image = io.imread(filename, as_gray=False)

angle = math.radians(45)
s = math.sin(angle)
c = math.cos(angle)

shape = image.shape


w = shape[1]
h = shape[0]

new_image = np.full(shape, 255, dtype = np.int16)

for i in range(0, w):
    for j in range(0, h):
        for m in range(1, 3):
          for n in range(1,3):
                x = j-w/2 + m/2
                y = i-h/2 + n/2
                
                new_x = np.int(x*c + y*s + w/2)
                new_y = np.int(y*c - x*s + h/2) 
                
                if(new_x < w and new_x >= 0 and new_y < h and new_y >= 0):
                    new_image[new_x, new_y,:] = image[j,i,:]  

fig, ax = plt.subplots(1, 1)
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.imshow(new_image, cmap=plt.cm.gray)
ax1.set_title('Rotada')
ax1.axis('off')

plt.show()