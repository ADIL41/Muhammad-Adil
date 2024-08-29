import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    _, frame= cap.read()

    #comvert BGR to HSV collor
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #threshold of blue in HSV space
    lower_blue=np.array([60,35,40])
    uper_blue= np.array([180,255,255])

    #preparing the mask to overlay
    mask=cv2.inRange(hsv,lower_blue,uper_blue)

#result
result=cv2.bitwise_and(frame,mask=mask)


cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()

    
