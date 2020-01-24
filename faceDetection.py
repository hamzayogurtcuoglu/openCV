import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while True:
	_,square = camera.read()
	gray = cv2.cvtColor(square,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors=5,minSize=(20,20))
	for (x,y,w,h) in faces:
		cv2.rectangle(square,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow("square",square)
	k = cv2.waitKey(1) &0xff
	if k == 27 or k == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()