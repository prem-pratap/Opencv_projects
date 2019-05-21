#!/usr/bin/env python3
import cv2
import time
cap=cv2.VideoCapture(0)
i=1
while cap.isOpened():
	status,frame=cap.read()
	while i <= 20:
		cv2.imshow('w_%d'%i,frame)
		cv2.imwrite('w_%d.jpg'%i,frame)
		i+=1			
		if cv2.waitKey(25) & 0xFF == ord('q'):
		        break
		
cv2.destroyAllWindows()
cap.release()
