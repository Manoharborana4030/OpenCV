import cv2
import datetime
cam=cv2.VideoCapture(0)
# print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))

# cam.set(3,1208)
# cam.set(4,720)
# print(cam.get(3))
# print(cam.get(4))
while(cam.isOpened()):
	ret,frame=cam.read()
	if ret:
		font=cv2.FONT_HERSHEY_SIMPLEX
		text='width: '+str(cam.get(3))+' Height '+str(cam.get(4))
		datet=str(datetime.datetime.now())
		frame=cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
		cv2.imshow("frame",frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cam.release()
cv2.destroyAllWindows()