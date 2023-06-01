import cv2
import numpy as np
import copy

cap=cv2.VideoCapture("a.mp4")
def nothing(x):
    print(x)
cv2.namedWindow("Tracking")
cv2.createTrackbar('LH',"Tracking",0,180,nothing)
cv2.createTrackbar('LS',"Tracking",0,255,nothing)
cv2.createTrackbar('LV',"Tracking",0,255,nothing)
cv2.createTrackbar('UH',"Tracking",180,180,nothing)
cv2.createTrackbar('US',"Tracking",255,255,nothing)
cv2.createTrackbar('UV',"Tracking",255,255,nothing)

while(cap.isOpened()):
    
    
    ret,frame=cap.read()
    f=copy.copy(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lH=cv2.getTrackbarPos('LH',"Tracking")
    lS=cv2.getTrackbarPos('LS',"Tracking")
    lV=cv2.getTrackbarPos('LV',"Tracking")

    uH=cv2.getTrackbarPos('UH',"Tracking")
    uS=cv2.getTrackbarPos('US',"Tracking")
    uV=cv2.getTrackbarPos('UV',"Tracking")
    l_bound=np.array([lH,lS,lV])
    #(200,0,0)
    u_bound=np.array([uH,uS,uV])
    mask=cv2.inRange(frame,l_bound,u_bound)

    frame=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("ghh",frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    tl=30
    tu=130
    f=cv2.Canny(frame,tl,tu)
    C=cv2.goodFeaturesToTrack(frame,25,0.01,10)
    C=np.int0(C)

    for i in C:
        x,y=i.ravel()
        cv2.circle(frame,(x,y),3,255,-1)
    cv2.imshow("hhhh",f)
    cv2.imshow("hhhjh",frame)
    cv2.waitKey(1)
