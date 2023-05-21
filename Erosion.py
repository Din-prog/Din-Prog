import cv2 
import numpy as np
import matplotlib.pyplot as plt


# read the image
img = cv2.imread(r".\\B.jpg", 0)

# binarize the image
# binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((5, 5), np.uint8)

# invert the image
invert = cv2. bitwise_not(binr)

# erode the image
erosion = cv2.erode(invert, kernel,
                    iterations=1)

# print the output
plt.imshow(erosion, cmap='gray')