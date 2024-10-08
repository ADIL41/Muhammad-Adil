import numpy as np
import cv2
from matplotlib import pyplot as plt 

img= cv2.imread('photos/2.jpg')

#Denoising of image
dst= cv2.fastNlMeansDenoisingColored(img,None,10,15,7,15)

#ploting
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
