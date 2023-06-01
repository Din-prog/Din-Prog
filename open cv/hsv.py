import cv2 
import numpy as np

cv2.imread('.\\B.jpg')
def nothing(x):
    print(x)

cv2.namedWindow("Tracking")

cv2.createTrackbar('LH', "Tracking",0,180, nothing)
cv2.createTrackbar('LS', "Tracking",0,255, nothing)
cv2.createTrackbar('LV', "Tracking",0,255, nothing)


cv2.waitKey()