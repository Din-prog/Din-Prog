import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcasede_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haaracasede_eye.xml')

img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in face:
    img = cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+w,ey+h),(0,255,0),2)

cv2.imshow('img', img)
cv2.waitKey()