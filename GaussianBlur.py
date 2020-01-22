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
# imaj , kernel , standard_sapma 
blur = cv2.GaussianBlur(imaj,(5,5),0)

cv2.imshow('imaj',imaj)
cv2.imshow('meanFilter',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('meanFilter',imaj.shape[1]+deltax,10)
while True:
    k = cv2.waitKey(10)&0xFF
    if k == 27 or k == ord("q"):
        break
cv2.destroyAllWindows()
        

