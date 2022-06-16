import cv2
cam=cv2.VideoCapture(0)
print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))

cam.set(3,1208)
cam.set(4,720)
print(cam.get(3))
print(cam.get(4))
while(cam.isOpened()):
	ret,frame=cam.read()
	if ret:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow("frame",gray)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cam.release()
cv2.destroyAllWindows()