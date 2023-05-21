import cv2
import numpy as np

#HSV (Hue saturation value )
# color detection using hsv colors 
def nothing(x):
    return 0
# cap=cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
#making trackbar (horizontal slider)
#[152,255,102]   --->  [180,255,255]
#[b,g,r][r,g,b][h,s,v]
cv2.createTrackbar('LH',"Tracking",0,180,nothing)
cv2.createTrackbar('LS',"Tracking",0,255,nothing)
cv2.createTrackbar('LV',"Tracking",0,255,nothing)
cv2.createTrackbar('UH',"Tracking",180,180,nothing)
cv2.createTrackbar('US',"Tracking",255,255,nothing)
cv2.createTrackbar('UV',"Tracking",255,255,nothing)

# cv2.namedWindow("Image")
# ImageTest=np.ones((512,512,3),np.uint8)
while(True):
    img=cv2.imread(".\\21.jpg")
    # ret,img=cap.read()
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #خواندن حد پایین
    #[h,s,v]
    lH=cv2.getTrackbarPos('LH',"Tracking")
    lS=cv2.getTrackbarPos('LS',"Tracking")
    lV=cv2.getTrackbarPos('LV',"Tracking")
    #خواندن حد بالا
    #[h,s,v]
    uH=cv2.getTrackbarPos('UH',"Tracking")
    uS=cv2.getTrackbarPos('US',"Tracking")
    uV=cv2.getTrackbarPos('UV',"Tracking")
    # سه رنگ را یک آرایه میکنیم
    #(100,0,0)
    l_bound=np.array([lH,lS,lV])
    #(200,0,0)
    u_bound=np.array([uH,uS,uV])

    mask=cv2.inRange(imghsv,l_bound,u_bound)

    res=cv2.bitwise_and(imghsv,imghsv,mask=mask)
    
    # imghsv=cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
    # cv2.imshow("Tracking",ImageTest)
    cv2.imshow("Image",img)
    cv2.imshow("ImageHSV",imghsv)
    cv2.imshow("res",res)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1)==27:
        break
# cap.release()


    canny = cv2.Canny(imghsv,100,200)
    # cv2.RETR_TREE => method
    # cv2.CHAIN_APPROX_SIMPLE => taghrib
    contours, hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('canny', canny)
cv2.destroyAllWindows()