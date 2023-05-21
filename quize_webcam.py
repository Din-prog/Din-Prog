import cv2
import numpy as np
from matplotlib import pyplot as plt
cam = cv2.VideoCapture(0)

# def show_webcam(mirror=False):
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret_val, img = cam.read()
#         if mirror: 
#             img = cv2.flip(img, 1)
#         cv2.imshow('my webcam', img)


gray = np.float32(cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY))
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None)

cam[dst>0.01*dst.max()]=[0,0,255]

edges = cv2.Canny(gray, treshold1=30, treshold2=150)

cv2.imshow('dst',cam)

if cv2.waitKey(1) == 27: 
    cv2.destroyAllWindows()