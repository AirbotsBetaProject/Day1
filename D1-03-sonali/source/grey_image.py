import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('grey_image.png', 0)  # read image and convert it into grey scale

cv2.imshow('image', img1)  # show image in grey scale 
cv2.waitKey(0)
cv2.destroyAllWindows()
