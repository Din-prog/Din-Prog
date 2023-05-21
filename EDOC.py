import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("B.jpg")
imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

l_b=np.array([6,55,184])
u_b=np.array([32,154,255])

mask=cv2.inRange(imghsv,l_b,u_b)
res=cv2.bitwise_and(imghsv,imghsv,mask=mask)

# imghsv=cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
cv2.imshow("img",img)
cv2.imshow("imghsv",imghsv)
cv2.imshow("res",res)
cv2.imshow("mask",mask)

# img2 = cv2.medianBlur(mask,3)
kernel = np.ones((3,3),np.uint8)
# erod = cv2.erode(mask,kernel)

erod = cv2.erode(mask,kernel,iterations=1)
# morph = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=5)
# morph1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel,iterations=1)
dilate = cv2.dilate(erod,kernel,iterations=1)

# cv2.imshow("res",img2)
cv2.imshow("dilate",dilate)
# cv2.imshow("CLOSE",morph)
# cv2.imshow("TOPHAT",morph1)

cv2.waitKey(0)
cv2.destroyAllWindows()
