import cv2
import numpy as np
import sys
import os

def resize(dst,img):
	width = img.shape[1]
	height = img.shape[0]
	dim = (width, height)
	resized = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)
	return resized

video = cv2.VideoCapture(1)
# bg = cv2.imread("D:\\Python\\OpenCV\\OpenCV\\data\\road.jpg")
black=cv2.VideoCapture('D:\\Python\\OpenCV\\OpenCV\\data\\5.mp4')
listImg = os.listdir("D:\\Python\\OpenCV\\OpenCV\\data\\BackgroundImages")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'D:\\Python\\OpenCV\\OpenCV\\data\\BackgroundImages\\{imgPath}')
    imgList.append(img)

print(imgList)
indexImg = 0
frame_counter=0
success, ref_img = video.read()
while(1):
        success, img = video.read()
        # success,bg = black.read()
        bg=imgList[indexImg]
        print(bg)
        bg = resize(bg,ref_img)
        diff1=cv2.subtract(img,ref_img)
        diff2=cv2.subtract(ref_img,img)
        diff = diff1+diff2
        diff[abs(diff)<14.0]=0
        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) < 10] = 0
        fgmask = gray.astype(np.uint8)
        fgmask[fgmask>0]=255
        fgmask_inv = cv2.bitwise_not(fgmask)
        fgimg = cv2.bitwise_and(img,img,mask = fgmask)
        bgimg = cv2.bitwise_and(bg,bg,mask = fgmask_inv)
        dst = cv2.add(bgimg,fgimg)
        cv2.imshow('Background Removal',dst)
        print(indexImg)
        key = cv2.waitKey(5) & 0xFF
        if key == ord('a'):
        	if indexImg>0:
        		indexImg -=1
        elif key == ord('d'):
        	if indexImg<len(imgList)-1:
        		indexImg +=1
        elif key == ord('q'):
        	break
        frame_counter += 1
        if frame_counter == black.get(cv2.CAP_PROP_FRAME_COUNT):
        	frame_counter = 0 
        	black.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyAllWindows()
video.release()