import cv2

cam=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter("testing.avi",fourcc,20.0,(640,480))
while(cam.isOpened()):
	ret,frame=cam.read()
	if ret:
		print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
		print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
		print(cam.get(cv2.CAP_PROP_POS_FRAMES))

		out.write(frame)
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow("frame",frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cam.release()
out.release()
cv2.destroyAllWindows()