import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('binary_hist.jpg', 0)  # read image


plt.hist(img.ravel(), 256, [0, 256])  # plot binary histogram for image in rgb
plt.show()  # display binary hisogram
