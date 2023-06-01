import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('.\\B.jpg',0)



#1:
plt.subplot(121)
plt.hist(img.ravel(),256,[0,256])
plt.subplot(122)
plt.imshow(img,'gray')
plt.show()

#2opencv:
# hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
# plt.subplot(121)
# plt.plot(hist_full)
# plt.subplot(122)
# plt.imshow(img,'gray')
# plt.show() 

# #3opencv:
# print(img.shape[:2])
# mask = np.zeros((img.shape[0],img.shape[1]),np.uint8)
# mask[100:400,300:600] =255
# masked_img = cv2.bitwise_and(img,img,mask=mask)    ##np.arrey
# hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
# hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
# plt.subplot(221)
# plt.imshow(img,'gray')
# plt.subplot(222)
# plt.imshow(mask,'gray')
# plt.subplot(223)
# plt.imshow(masked_img,'gray')
# plt.subplot(224)
# plt.plot(hist_full)
# plt.plot(hist_mask)
# plt.xlim([0,256])
# plt.show() 


#4:
color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col) 
cv2.imshow('img',img)
plt.show()
