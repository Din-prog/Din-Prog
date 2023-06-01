import cv2
import numpy as np 

image = cv2.imread('geeks.png')

image1 = cv2.medianBlur(image, 11)
image3 = cv2.GaussianBlur(image,(5,5),0)
kernel = [
    [2,0,-2],
    [2,0,-2],
    [2,0,-2]
]
image2 = cv2.filter2D(image,-1,kernel=np.array(kernel))


cv2.imshow('0',image)
cv2.imshow('1',image3)

cv2.waitKey()
cv2.destroyAllWindows()