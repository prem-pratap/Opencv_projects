#!/usr/bin/env python3
import cv2
cap=cv2.VideoCapture(0)
#saving two images one with obstacle and another without obstacle
while cap.isOpened():
    status,f1=cap.read()
    cv2.imshow("Without Obstacle",f1)
    cv2.imwrite("obj1.jpg",f1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
while cap.isOpened():
    status,f2=cap.read()
    cv2.imshow("With Obstacle",f2)
    cv2.imwrite("obj2.jpg",f2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#reading two images that were saved
pic1=cv2.imread("obj1.jpg")
pic2=cv2.imread("obj2.jpg")
#give the different region from both the images
diff=cv2.subtract(pic1,pic2)
#saving the different image 
cv2.imwrite('result.jpg',diff)
mask = cv2.imread('result.jpg',0)
#filling regions inside image
dst = cv2.inpaint(pic1,mask,0.4,cv2.INPAINT_TELEA)
cv2.imwrite('painted.jpg',dst)
img=cv2.imread("painted.jpg")
#add painted image and image without obstacle along with weights
new_img=cv2.addWeighted(pic1,0.6,img,0.4,0)
cv2.imshow('new image',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey()
cap.release()
