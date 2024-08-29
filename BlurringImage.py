import cv2
import numpy as np

img = cv2.imread('photos/6.jpg')
img= cv2.resize(img,(500,500))

cv2.imshow('original',img)
cv2.waitKey(0)

#Gaussian Blur
Gaussian=cv2.GaussianBlur(img,(9,9),0)
cv2.imshow('gaussian blurring',Gaussian)
cv2.waitKey(0)

#Median blur
median=cv2.medianBlur(img,9)
cv2.imshow('median blur',median)
cv2.waitKey(0)

#Bilateral Blur
Bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral image',Bilateral)
cv2.waitKey(0)






