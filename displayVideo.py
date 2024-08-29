import cv2
import numpy as np

cap=cv2.VideoCapture('videos/Cars.mp4')

while True:
    ret, frame=cap.read()

    cv2.imshow('video',frame)

    if cv2.waitKey(0) == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()


  
    