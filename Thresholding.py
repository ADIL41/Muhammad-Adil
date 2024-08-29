import cv2
import numpy as np

img = cv2.imread('photos/6.jpg')
img=cv2.resize(img,(500,500))

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#applying thresholding 

thresh1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,7)


thresh2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,7)
cv2.imshow('thresh_mean',thresh1)
cv2.imshow('thresh_guassian',thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
