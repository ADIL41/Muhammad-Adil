import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    cv2.waitKey(0) 
    

  
cap.release()
cv2.destroyAllWindows()




