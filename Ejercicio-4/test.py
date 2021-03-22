import matplotlib
import matplotlib.pyplot as plt

import numpy as np

a = np.zeros([300, 300])

s = a.shape

for i in range(0,s[0]):
    for j in range(0,s[1]):
        if(j%100 >= 50 and i%100 >= 50):
            a[i,j] = 1
        else:
            a[i,j] = -1

transform = np.fft.rfft2(a, norm="ortho")

transformM = np.abs(transform).astype('float64')

m = 1/(transformM.min() - transformM.max())
b = 1-m*transformM.min()

for i in range(0, transformM.shape[0]):
    for j in range(0, transformM.shape[1]):
        transformM[i,j] *= m
        transformM[i,j] += b
        
fig, ax = plt.subplots(1, 1)
ax.imshow(a, cmap=plt.cm.gray)
ax.set_title('Original')
ax.axis('off')

fig1, ax1 = plt.subplots(1, 1)
ax1.imshow(transformM, cmap=plt.cm.gray)
ax1.set_title('Transformada de Fourier')
plt.xlim(0,50)
plt.ylim(0,50)

plt.show()