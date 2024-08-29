import cv2
import numpy as np

img= cv2.imread('photos/10.jpg')
B, G, R= cv2.split(img)
img= cv2.resize(img,(400,400))
cv2.imshow("original",img)
cv2.waitKey(0)

cv2.imshow("blue",B)
cv2.waitKey(0)


cv2.imshow("green",G)
cv2.waitKey(0)

cv2.imshow("red",R)
cv2.waitKey(0)

cv2.destroyAllWindows()



