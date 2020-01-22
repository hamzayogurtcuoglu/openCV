import cv2
import numpy as np
import sys


imaj = cv2.imread("resim.png")
# imaj , kernel , standard_sapma 

kernel = np.ones((5,5),np.uint8)
#sınırları inceltme
erosion = cv2.erode(imaj,kernel,iterations=1)
#sınırları kalınlaştırma
dilation = cv2.dilate(imaj,kernel,iterations=1)
dusey = np.vstack((imaj,erosion,dilation))
cv2.imshow('imaj',imaj)
cv2.imshow('dusey',dusey)
cv2.moveWindow('imaj',10,10)
while True:
    k = cv2.waitKey(10)&0xFF
    if k == 27 or k == ord("q"):
        break
cv2.destroyAllWindows()
        

