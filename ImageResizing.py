import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('photos/2.jpg')
# Loading the image

half = cv2.resize(image, (0, 0), fx = 0.2, fy = 0.2)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (782, 542), 
               interpolation = cv2.INTER_LINEAR)


Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()
