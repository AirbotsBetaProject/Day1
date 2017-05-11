import cv2
import numpy as np
import matplotlib.pyplot as plt

pic_num = 1
x = np.arange(0, 256)
cam = cv2.VideoCapture(0)  # open video camera
for k in range(0, 100):  # capture 100 frames
    ret, frame = cam.read()  # read frames from camera feed
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # write gray images into new files
    cv2.imwrite('outputpics/'+str(pic_num)+'.jpg', img)
    # empty array of zeroes for counting number of pixels with particular
    # intensity
    hist = np.zeros(256)
    for i in range(0, img.shape[0]):  # for every row
        for j in range(0, img.shape[1]):  # for every column in a row
            temp = img[i, j]  # get pixel intensity
            hist[temp] += 1  # increment the count for that intensity
    plt.plot(x, hist)  # show the histogram
    plt.xlabel('intensity')
    plt.ylabel('count')
    # save the histogram in output folder outputhist
    plt.savefig('outputhist/'+str(pic_num)+'.jpg')
    pic_num += 1
    plt.gcf().clear()  # clear histogram plot to avoid overwriting
cam.release()  # close the camera
