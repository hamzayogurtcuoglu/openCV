import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 

out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))
 
while(True):
  ret, frame = cap.read()
 
  if ret == True: 
     
    out.write(frame)
 
    cv2.imshow('frame',frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  else:
    break 
 
cap.release()
out.release()
 
cv2.destroyAllWindows() 	
