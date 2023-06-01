import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('.\\corner.webp')
gray = np.float32(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corner, not important
dst = cv2.dilate(dst,None)
# cv2.imshow('dst',dst)
# Threshold for an optimal value, it may vary depending on the image
a = img[dst>0.01*dst.max()]=[0,0,255]


cv2.imshow('dst',img)
# harris    =    [(x+y, y+h)-(x,y)]tavan2
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
