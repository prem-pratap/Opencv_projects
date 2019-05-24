import cv2
import numpy as np

windowName = 'Drawing Demo'

img =cv2.imread("obj2.jpg")
cv2.namedWindow(windowName)

# true if mouse is pressedF
drawing = False

# if
(ix, iy) = (-1, -1)

# mouse callback function
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

cv2.setMouseCallback(windowName, draw_shape)

def main():
    global mode
    
    while(True):
        cv2.imshow(windowName, img)
        k = cv2.waitKey(1)
        if k == 27:
                cv2.imwrite("paint.jpg",img)
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
