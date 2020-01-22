import cv2

reswh = [(1920,1080),(1600,900),(1366,768),(1280,720),(1024,576),(960,544),(640,480),(320,240)]

def main():
	camera = cv2.VideoCapture(0)
	for j in range(len(reswh)):
		w0 = int(reswh[j][0])
		h0 = int(reswh[j][1])
		camera.set(3,w0)
		camera.set(4,h0)
		w1 = camera.get(3)
		h1 = camera.get(4)
		print(f"Test : ({w0},{h0}) Result: ({w1},{h1})")
		res,square = camera.read()
		cv2.imshow("res",square)
		k = cv2.waitKey(3000)&0xff
	if camera.isOpened():
		camera.release()
	cv2.destroyAllWindows()





if __name__== "__main__":
	main()