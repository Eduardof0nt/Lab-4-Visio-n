import matplotlib
import matplotlib.pyplot as plt

from skimage import data
from skimage.filters import try_all_threshold

from skimage import io
import os

filename = os.getcwd() + '/Ejercicio-1/Img/Ejercicio1-a.jpeg'

img = io.imread(filename, as_gray=True)

fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=True)
plt.show()