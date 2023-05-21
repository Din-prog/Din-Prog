import cv2 
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('\\.B.jpg')
imghsv = cv2.cvtcolor(img,cv2.COLOR_BGR2HSV)

l_b = np.array([6,55,184])
u_b = np.array([32,154,255])

mask = cv2.inRange