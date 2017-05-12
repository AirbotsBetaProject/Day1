import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('edit.jpg')
cv2.imshow('image',img)

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.xlabel('Pixel intensity')
    plt.ylabel('No of pixels')
plt.show()
