import cv2
import numpy as np
import sys

if sys.platform =='win32':
    deltax = 0
    deltay = 0
else:
    deltax = 50
    deltay = 105

imaj = cv2.imread("resim.png")
# imaj ,komşuluk_çapı_sigma_renk,sigma_uzay 
gray =cv2.cvtColor(imaj,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(7,7),0)
canny =cv2.Canny(blur,0,30)
canny = cv2.bitwise_not(canny)
imaj = cv2.bitwise_and(imaj,imaj,mask = canny)



cv2.imshow('imaj',imaj)
cv2.imshow('Edge',canny)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('Edge',imaj.shape[1]+deltax,10)
while True:
    k = cv2.waitKey(10)&0xFF
    if k == 27 or k == ord("q"):
        break
cv2.destroyAllWindows()
        

