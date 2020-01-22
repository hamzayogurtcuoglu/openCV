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
n = 3 
kernel = np.ones((n,n),np.float32)/(n*n*1.0)

blur = cv2.filter2D(imaj,-1,kernel)

cv2.imshow('imaj',imaj)
cv2.imshow('filter2D',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('filter2D',imaj.shape[1]+deltax,10)
while True:
    k = cv2.waitKey(10)&0xFF
    if k == 27 or k == ord("q"):
        break
cv2.destroyAllWindows()
        

