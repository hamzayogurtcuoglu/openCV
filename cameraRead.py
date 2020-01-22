import cv2

def main():
	camera = cv2.VideoCapture(0)
	while(True):
		ret,square = camera.read()
		if not ret:
			break
		cv2.imshow('kare',square)
		cv2.moveWindow('kare',10,10)
		k=cv2.waitKey(3000)&0xff
		if k == 27 or k == ord('q'):
			break
		if camera.isOpened():
			camera.release()
		cv2.destroyAllWindows()

if __name__== "__main__":
	main()