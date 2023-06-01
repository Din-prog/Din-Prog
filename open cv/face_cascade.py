# Importing OpenCV package
import cv2
  
# Reading the image
img = cv2.imread('.\\B.jpg')

# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml")
print(cv2.data.haarcascades) 
# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img)
eyes_rect = eye_cascade.detectMultiScale(gray_img,1.1,6)
# 1.1,1.2,1.3

while True:
        # Converting image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Loading the required haar-cascade xml classifier file
    haar_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml")
    print(cv2.data.haarcascades) 
    # Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img)
    eyes_rect = eye_cascade.detectMultiScale(gray_img,1.1,6)
    # Iterating through rectangles of detected faces
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    img[x:x+w,y:y+h]  = stiker

for (x, y, w, h) in eyes_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
cv2.imshow('Detected faces', img)

cv2.waitKey(0)