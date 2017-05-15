import cv2
import numpy as np
from matplotlib import pyplot as plt
#converting image to gray
myimg=cv2.imread('chil.jpg',0)
cv2.imshow('myimg',myimg)
#plotting histogram
plt.hist(myimg.ravel(),256,[0,256]); plt.show()
cv2.waitKey(0)
