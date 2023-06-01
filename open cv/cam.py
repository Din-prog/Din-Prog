import cv2

# cap = cv2.VideoCapture('tom and jerry.mp4')
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

video = cv2.VideoCapture(0)
if (video.isOpened() == False):
    print('Error...')
frame_wight = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_wight,frame_height)
result = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,size)
while (True):
    ret, frame = video.read()
    if ret == True:
        result.write(frame)
        cv2.imshow('fram',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
       break
    else:
        break
video.release()
result.release()
cv2.destroyAllWindows()