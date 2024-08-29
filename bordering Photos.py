import cv2
import numpy as np

img = cv2.imread('photos/6.jpg')
img=cv2.resize(img,(500,500))

img=cv2.copyMakeBorder(img,50,50,20,20,cv2.BORDER_CONSTANT,None,value=0)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#refecting frame

img = cv2.copyMakeBorder(img, 100, 100, 50, 50, cv2.BORDER_REFLECT) 
  
# Displaying the image  
cv2.imshow('refelct Image', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

