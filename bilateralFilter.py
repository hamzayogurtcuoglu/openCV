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
blur = cv2.bilateralFilter(imaj,11,175,175)

cv2.imshow('imaj',imaj)
cv2.imshow('bileteralFilter',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('bileteralFilter',imaj.shape[1]+deltax,10)
while True:
    k = cv2.waitKey(10)&0xFF
    if k == 27 or k == ord("q"):
        break
cv2.destroyAllWindows()
        

