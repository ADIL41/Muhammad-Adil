import cv2
import numpy as np

img= cv2.imread('photos/5.jpg')
img= cv2.resize(img,(600,600))

img= cv2.line(img,(0,0),(255,255),(55,25,147),thickness=10)      #draw a line in an image

img= cv2.arrowedLine(img,(0,255),(200,200),(255,0,0),thickness=2)   #draw an arrowline in image

img= cv2.rectangle(img,(385,0),(500,105),(0,0,255),thickness=8)    # draw a rectangle in am image

img= cv2.circle(img,(375,240),(70),(255,0,0),thickness=10)     #draw a circle in an image

font=cv2.FONT_HERSHEY_SIMPLEX  # variable for font style

img= cv2.putText(img,(' Adil'),(10,500),(font),(5),(100,255,33),thickness=5) #write a text on image


cv2.imshow('image',img)

cv2.waitKey()
cv2.destroyAllWindows()
