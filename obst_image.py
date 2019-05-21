#!/usr/bin/env python3
import cv2
import numpy
pic1=cv2.imread("r1.jpg")
pic2=cv2.imread("r2.jpg")
diff=cv2.subtract(pic1,pic2)
cv2.imwrite('result.jpg',diff)
mask = cv2.imread('result.jpg',0)
'''
inpaint(src,binary mask indicating area to inpainted,inpaint radius(Neighborhood around a pixel to inpaint. 
Typically, if the regions to be inpainted are thin, smaller values produce better results (less blurry),flags(INPAINT_NS/INPAINT_TELEA)))
'''
#cv2.imshow("result",mask)
cv2.waitKey()
dst = cv2.inpaint(pic1,mask,0.5,cv2.INPAINT_TELEA)
cv2.imwrite('dst.jpg',dst)
re=cv2.imread("dst.jpg")
cv2.imshow("dst",re)
cv2.waitKey()
new_img=cv2.addWeighted(pic1,0.5,re,0.5,0)
cv2.imshow('new image',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey()
