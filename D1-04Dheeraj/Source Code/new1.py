import numpy as np
import cv2, matplotlib.pyplot as plt

img=cv2.imread('athens.jpg',0)
plt.hist(img.ravel(),256,[0,256])
plt.show()
plt.savefig('histogram.jpg')


