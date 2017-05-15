import cv2
import numpy as np
from matplotlib import pyplot as nani
img = cv2.imread('leo.jpg', 0)
nani.hist(img.ravel(), 256, [0, 256])
nani.show()