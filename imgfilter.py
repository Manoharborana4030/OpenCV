import cv2
import numpy as np


img=cv2.imread("pic.png")
kernel=np.ones((5,5),np.uint8)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(img,(7,7),0)
imgcanny=cv2.Canny(img,100,100)
imgdilation=cv2.dilate(imgcanny,kernel,iterations=1)
imgErode=cv2.erode(imgdilation,kernel,iterations=1)

cv2.imshow("gray Image",imgray)
cv2.imshow("blur img",imgblur)
cv2.imshow("Canny img",imgcanny)
cv2.imshow("Img dilatea",imgdilation)
cv2.imshow("Img Erode",imgErode)

cv2.waitKey(0)

