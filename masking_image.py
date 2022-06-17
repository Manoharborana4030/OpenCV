import cv2
import numpy as np

img=cv2.imread('OpenCV\\OpenCV\\pic.jpg')
img2=cv2.imread('OpenCV\\OpenCV\\two.png')
# img=cv2.resize(img,(720,500))
print(img.shape)
print(img.dtype)
print(img.size)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))	

glass=img[290:340,330:390]
img[283:333,100:160]=glass

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
# dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,.9,img2,.9,0)

cv2.imshow('Image',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()