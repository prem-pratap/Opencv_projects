#!usr/bin/env python3
import cv2
cap=cv2.VideoCapture("https://192.168.43.1:8080/video")
while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow("IPWEBCAM",frame)
	if cv2.waitKey(25) & 0xFF== ord('q'):
		break;
cv2.destroyAllWindows()
cap.release()
