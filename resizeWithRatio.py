import cv2
import random

imaj = cv2.imread("resim.png")
cv2.imshow('imaj',imaj)
oran = 0.25
imajlar = []

#oran = random.randint(1,25)/25
rx = int(imaj.shape[1]*oran)
ry = int(imaj.shape[0]*oran)

x = random.randint(100,1600)
y = random.randint(100,800)

imajlar.append((str(oran),cv2.resize(imaj,(rx,ry))))
cv2.imshow(imajlar[0][0],imajlar[0][1])
cv2.moveWindow(imajlar[0][0],x,y)

while True:
    k = cv2.waitKey(50)&0xFF
    if k==27:
        break
cv2.destroyAllWindows()
