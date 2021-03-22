import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from skimage import io
import os

import math

image = io.imread(os.getcwd() + '/Ejercicio-4/Img/ruido04.jpg', as_gray=True)

print(image.shape)

transform = np.fft.rfft2(image)

transformM = np.abs(transform).astype('float64')

m = 1/(transformM.min() - transformM.max())
b = 1-m*transformM.min()

for i in range(0, transformM.shape[0]):
    for j in range(0, transformM.shape[1]):
        transformM[i,j] *= m
        transformM[i,j] += b
# transformP = np.angle(transform)

def lowPass2D(x, y, w0):
    return w0/(w0 + 1j*(x**2 + y**2)**0.5)

def highPass2D(x, y, w0):
    return -(1j*(x**2 + y**2)**0.5)/(w0 + 1j*(x**2 + y**2)**0.5)

shape = transform.shape

transform1 = transform.copy()
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        transform1[i,j] *= lowPass2D(i,j,20)

filterImg1 = np.fft.irfft2(transform1)

transform2 = transform.copy()
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        transform2[i,j] *= highPass2D(i,j,1) 

filterImg2 = np.fft.irfft2(transform2)

transform3 = transform.copy()
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        transform3[i,j] *= lowPass2D(i,0,20)

filterImg3 = np.fft.irfft2(transform3)

transform4 = transform.copy()
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        transform4[i,j] *= highPass2D(0,j,1)

filterImg4 = np.fft.irfft2(transform4)

fig, ax = plt.subplots(1, 1)
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.imshow(transformM, cmap=plt.cm.gray)
ax1.set_title('Transformada de Fourier')
plt.xlim(0,50)
plt.ylim(0,50)

fig2, ax2 = plt.subplots(1, 1)
ax2.imshow(filterImg1, cmap=plt.cm.gray)
ax2.set_title('Filtro Pasa Bajas')
ax2.axis('off')

fig3, ax3 = plt.subplots(1, 1)
ax3.imshow(filterImg2, cmap=plt.cm.gray)
ax3.set_title('Filtro Pasa Altas')
ax3.axis('off')

fig4, ax4 = plt.subplots(1, 1)
ax4.imshow(filterImg3, cmap=plt.cm.gray)
ax4.set_title('Filtro Pasa Bajas Vertical')
ax4.axis('off')

fig5, ax5 = plt.subplots(1, 1)
ax5.imshow(filterImg4, cmap=plt.cm.gray)
ax5.set_title('Filtro Pasa Altas Horizontal')
ax5.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.hist(image.ravel(), bins=256, histtype='step', color='black', density=True)
ax1.set_title('Histograma Original')

plt.show()