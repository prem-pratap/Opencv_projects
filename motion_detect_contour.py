import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture("/home/prempratap/Desktop/ML/move.mp4") 
while cap.isOpened():
    status,frame1=cap.read()
    status,frame2=cap.read()
    d=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    check,thresh_delta=cv2.threshold(blur,30,255,cv2.THRESH_BINARY)
    thresh_dilated=cv2.dilate(thresh_delta ,np.ones((2,2),np.uint8), iterations=1)
    img,c,h=cv2.findContours(thresh_dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.drawContours(frame1,c,-1,(0,255,0),2)
    cv2.imshow("motion",frame1)
    
    if cv2.waitKey(30) & 0xff ==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
