import cv2 
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread('photos/10.jpg', cv2.IMREAD_GRAYSCALE)

edges=cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('original image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

