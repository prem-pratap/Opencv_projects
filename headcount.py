#!/usr/bin/env python3

import  cv2
import numpy as np
import os
cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture("https://192.168.43.1:8080/video")
#Trainnig our classifier for face detection using haar file(.xml)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
font=cv2.FONT_ITALIC
while cap.isOpened():
	status,frame=cap.read()
	#grayimg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(frame,1.15,5) 
	for  (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) 
		#fo_gray=grayimg[y:y+h,x:x+w]
		#fo_color=frame[y:y+h,x:x+w]
	
	msg="Face Detected="+str(len(faces))
	#puttext(image,msg,(coordinate),fonttype,fontscale,fontcolor,linetype
	cv2.putText(frame,msg,(10,50),font,1,(120,0,255),3,cv2.LINE_AA)	
	cv2.imshow('Detect',frame)
	#cv2.imshow('Gray',fo_gray)
	#cv2.imshow('FaceOnly',fo_color)
	if cv2.waitKey(30) & 0xff ==ord('q'):
		break		
voice_output="echo Headcount was "+str(len(faces))+" | festival --tts"
os.system(voice_output)
cv2.destroyAllWindows()
cap.release()
'''
cv2.imshow('gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
    minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it
'''
