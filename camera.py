#!/usr/bin/env python3
import cv2
#to start camera
cap=cv2.VideoCapture(0) # 0 for default camera
while cap.isOpened():
	status,frame=cap.read()
	#gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('w',frame)  #to add filter frame+50 i.e. BGR+50
	#cv.imshow('w1',gray_frame)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
