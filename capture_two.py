#!usr/bin/env python3
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while cap.isOpened():
	status,f1=cap.read()
	status,f2=cap.read()
	cv2.imshow("live",f1)	
	cv2.imwrite("i_1.jpg",f1)
	cv2.imwrite("i_2.jpg",f2)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
p1=cv2.imread('i_1.jpg',1)
p2=cv2.imread('i_2.jpg',1)		
nhorizontal=np.hstack((p1,p2))#to combine to array
cv2.imshow("combined",nhorizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

