#!/usr/bin/env pythonnv 3

import  cv2
#  starting camera
cap=cv2.VideoCapture(0)
#  deciding  video format 
fourcc=cv2.VideoWriter_fourcc(*'XVID') #it gives a flag which matches with the given format 
output=cv2.VideoWriter('myvide1.avi',fourcc,2,(848,480))

while cap.isOpened():

	# reading frames
	status,frame=cap.read()
	#gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('live',frame)
	output.write(frame)
	if cv2.waitKey(23) &  0xff ==  ord('q') :
		break

cv2.destroyAllWindows()
cap.release()
