#!/usr/bin/env python3
import cv2 
#to start camera
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('cl1.jpg',frame)
    display=cv2.merge([frame,gray_frame])
    cv2.imshow('w1',frame)
    cv2.imshow('w2',gray_frame)
    cv2.imshow('w3',display)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
