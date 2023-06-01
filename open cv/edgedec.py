import cv2
import numpy as np
from matplotlib import pyplot as plt

# read the image 
img = cv2.imread('.\\corner.webp')

# Setting parameter values
treshold_lower = 30  # lower treshold
treshold_upper = 150 # upper treshold

# convert it to graycale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying the  Canny Edge filter
edges = cv2.Canny(gray, treshold_lower, treshold_upper)
cv2.imshow("Ddd",edges)


cv2.waitKey()
