from __future__ import print_function
import numpy as np
import cv2 
import argparse
import random 

color = random.seed(12345)

def thresh_callback(val):
    threshold = val

    # Detect edges using Canny
    canny_output = cv2.Canny(src_gray, threshold, threshold * 2)

    # Find contours
    _, contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contour
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0)

    # Show in a window
    cv2.imshow('Contour', drawing)

# Load source image
parser = argparse.ArgumentParser(description='Code for Finding contours in your image tutorial.')
parser.add_argument('--input', help='path to input umage', default='B.jpg')
args = parser.parse_args()

src = cv2.imshow(cv2.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image', args.input)
    exit(0)

# Convert image to gray and blur it
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
src_gray = cv2.blur(src_gray, (3, 3))

# Create Window
source_window = 'source'
cv2.namedWindow(source_window)
cv2.imshow(source_window, src)
max_thresh = 255
thresh = 100
# initial threshold
cv2.createTrackbar('Canny Thresh', source_window, thresh, max_thresh, thresh_callback)