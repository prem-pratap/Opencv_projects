import cv2
import numpy as np

#obstacles removal with HSV

#function to draw at coordinates of event
def draw(event,x,y,flags,parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(pic,(x,y),5,(255,255,255),-1)#to draw circle at coordinates
    elif event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(pic,(x,y),5,(255,255,255),-1)#to draw circle at coordinates
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(pic,(x,y),5,(255,255,255),-1)#to draw circle at coordinates

cap=cv2.VideoCapture(0)
#saving main image
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow("Main Frame",frame)
    if cv2.waitKey(30) & 0xff==ord('q'):
        cv2.imwrite("Main.jpg",frame)
        break
        
window="draw"
cv2.namedWindow("draw")    
pic=cv2.imread("Main.jpg")
cv2.setMouseCallback(window,draw)#call function to draw on window

while True:
    cv2.imshow(window,pic)
    if cv2.waitKey(30) & 0xff==ord('w'):
        cv2.imwrite("Final.jpg",pic)
        break
    elif cv2.waitKey(30) & 0xff==ord('r'):
        pic=cv2.imread("Main.jpg")
        pass
#draw panel for setting hsv value
cv2.namedWindow("panel")
panel=np.zeros([100,70,3],np.uint8)
def nothing(x):
    pass
cv2.createTrackbar("L-h","panel",0,255,nothing)
cv2.createTrackbar("U-h","panel",255,255,nothing)
cv2.createTrackbar("L-s","panel",0,255,nothing)
cv2.createTrackbar("U-s","panel",255,255,nothing)
cv2.createTrackbar("L-v","panel",0,255,nothing)
cv2.createTrackbar("U-v","panel",255,255,nothing)
while True:
    img=cv2.imread("Final.jpg")
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("L-h","panel")
    u_h=cv2.getTrackbarPos("U-h","panel")
    l_s=cv2.getTrackbarPos("L-s","panel")
    u_s=cv2.getTrackbarPos("U-s","panel")
    l_v=cv2.getTrackbarPos("L-v","panel")
    u_v=cv2.getTrackbarPos("U-v","panel")
    
    low=np.array([l_h,l_s,l_v])
    upper=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,low,upper)#return pixels found in range
    fg=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("fg",fg)
    if cv2.waitKey(30) & 0xff==ord('w'):
        cv2.imwrite("mask.jpg",fg)
        break
mask = cv2.imread('mask.jpg',0)
#filling regions inside image
painted = cv2.inpaint(img,mask,0.4,cv2.INPAINT_TELEA)
cv2.imwrite('painted.jpg',painted)
removed=cv2.imread("painted.jpg")
cv2.imshow("REMOVED",removed)
cv2.waitKey()
cv2.destroyAllWindows()
cap.release()

