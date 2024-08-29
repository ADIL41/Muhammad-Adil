import cv2
import numpy as np

img=cv2.imread('photos/1.jpg',)   #load an image

cv2.imshow('cat',img)    #display an image

cv2.waitKey()

cv2.destroyAllWindows()
