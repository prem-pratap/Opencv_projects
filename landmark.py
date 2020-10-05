#!/usr/bin/env python3 
import cv2
import face_recognition

cap=cv2.VideoCapture(0)
while cap.isOpened():
	status,f1=cap.read()
	face_landmarks_list = face_recognition.face_landmarks(f1)
	cv2.imshow("landmark",f1)
	if cv2.waitKey(30) & 0xff==ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
