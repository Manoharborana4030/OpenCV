import cv2
import numpy as np

img=cv2.imread("pic.png",1)#1 for colored image,0 for grey image,-1 alpha chanale like no changed... 

#this is for open any image file in window 
cv2.imshow("Image",img)

#this will open window till 5 seconds
key=cv2.waitKey(0)

#27 for ESC button 
if key==27:
	print("you hitt.. ESC button ")
	cv2.destroyAllWindows()	
elif key==ord('s'):
	print("you hitt.. S button ")
	cv2.imwrite('Copy_Manu.png',img)
	print("Your file saved....")




