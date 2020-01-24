import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade_smile.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

camera = cv2.VideoCapture(0)

out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))

while True:
	ret,square = camera.read()
	gray = cv2.cvtColor(square,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors=3,minSize=(20,20))
	for (x,y,w,h) in faces:
		cv2.rectangle(square,(x,y),(x+w,y+h),(255,0,0),2)
		grayBox = gray[y:y+h,x:x+w]
		colorBox = square[y:y+h,x:x+w]
		
		smiles = smileCascade.detectMultiScale(grayBox,scaleFactor = 1.5,minNeighbors=18,minSize=(30,30))
		for (ex,ey,ew,eh) in smiles:
			cv2.rectangle(colorBox,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

		eyes = eyeCascade.detectMultiScale(grayBox,scaleFactor = 1.5,minNeighbors=6,minSize=(3,3))
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(colorBox,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	
	if ret == True:
		out.write(square)
	else:
		break 
	cv2.imshow("square",square)
	


	k = cv2.waitKey(10) &0xff
	if k == 27 or k == ord("q"):
		break
out.release()
camera.release()
cv2.destroyAllWindows()