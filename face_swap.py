#!/usr/bin/env python3
import cv2
import numpy as np
import dlib

image1=cv2.imread("./pic1.jpg")
gray1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
image2=cv2.imread("./pic2.jpg")
gray2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
img2_new_face=np.zeros_like(image2)
#function to find index of landmark in nparray for pic2
def index_points(array):
    index=None 
    for num in array[0]:
        index=num 
        break
    return index
detector=dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
landmark_points=[]
landmark_points2=[]
final_landmark_points=[]
index_triangles=[]#this will have landmark points which need to be connected to form triangle

#np.zeroes means and image completely black
mask=np.zeros_like(gray1)
faces=detector(gray1)
for face in faces:
    landmarks=predictor(gray1,face)
    for i in range(0,68):
        x=landmarks.part(i).x
        y=landmarks.part(i).y
        landmark_points.append((x,y))
        #cv2.circle(image1,(x,y),3,(0,0,255),-1)  #circles to show the landmarks points
points=np.array(landmark_points,np.int32)
hull=cv2.convexHull(points)
#polylines to show the convexhull around the points
#cv2.polylines(image1,[hull],True,(0,0,255),3)

cv2.fillConvexPoly(mask,hull,255)
face_image=cv2.bitwise_and(image1,image1,mask=mask)
rect=cv2.boundingRect(hull)
subdiv=cv2.Subdiv2D(rect)
subdiv.insert(landmark_points)
triangles=subdiv.getTriangleList()
triangles=np.array(triangles,dtype=np.int32)
for t in triangles:
    pt1=(t[0],t[1])
    pt2=(t[2],t[3])
    pt3=(t[4],t[5])
    #to show triangulation in image1
    #cv2.line(face_image,pt1,pt2,(0,0,255),1)
    #cv2.line(face_image,pt2,pt3,(0,0,255),1)
    #cv2.line(face_image,pt1,pt3,(0,0,255),1)
    index_pt1=np.where((points==pt1).all(axis=1))
    index_pt1=index_points(index_pt1)
    index_pt2=np.where((points==pt2).all(axis=1))
    index_pt2=index_points(index_pt2)
    index_pt3=np.where((points==pt3).all(axis=1))
    index_pt3=index_points(index_pt3)
    if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
        triangle=[index_pt1,index_pt2,index_pt3]
        index_triangles.append(triangle)
#for second face
faces2=detector(gray2)
for face in faces2:
    landmarks=predictor(gray2,face)
    for i in range(0,68):
        x=landmarks.part(i).x
        y=landmarks.part(i).y
        landmark_points2.append((x,y))

for triangle_index in index_triangles:
    #triangulation of first image
    tr1_pt1=landmark_points[triangle_index[0]]
    tr1_pt2=landmark_points[triangle_index[1]]
    tr1_pt3=landmark_points[triangle_index[2]]
    
    #to show triangulation in image1
    #cv2.line(image1,tr1_pt1,tr1_pt2,(255,0,0),1)
    #cv2.line(image1,tr1_pt2,tr1_pt3,(255,0,0),1)
    #cv2.line(image1,tr1_pt1,tr1_pt3,(255,0,0),1)
    triangle1=np.array([tr1_pt1,tr1_pt2,tr1_pt3],np.int32)
    rect1=cv2.boundingRect(triangle1)
    (x,y,w,h)=rect1
    cropped_triangle=image1[y:y+h,x:x+w]
    cropped_tri_mask=np.zeros((h,w),np.uint8)
    points=np.array([[tr1_pt1[0]-x,tr1_pt1[1]-y],[tr1_pt2[0]-x,tr1_pt2[1]-y],
                     [tr1_pt3[0]-x,tr1_pt3[1]-y]],np.int32)
    cv2.fillConvexPoly(cropped_tri_mask,points,255)
    cropped_triangle=cv2.bitwise_and(cropped_triangle,cropped_triangle,mask=cropped_tri_mask)
    #cv2.imshow("rectangl1",image1[y:y+h,x:x+w]) to show only rectangle around first triangle
    #triangulation of second image
    tr2_pt1=landmark_points2[triangle_index[0]]
    tr2_pt2=landmark_points2[triangle_index[1]]
    tr2_pt3=landmark_points2[triangle_index[2]]
    #to show triangulation in image2
    #cv2.line(image2,tr2_pt1,tr2_pt2,(255,0,0),1)
    #cv2.line(image2,tr2_pt2,tr2_pt3,(255,0,0),1)
    #cv2.line(image2,tr2_pt1,tr2_pt3,(255,0,0),1)
    triangle2=np.array([tr2_pt1,tr2_pt2,tr2_pt3],np.int32)
    rect2=cv2.boundingRect(triangle2)
    (x,y,w,h)=rect2
    cropped_triangle2=image2[y:y+h,x:x+w]
    cropped_tri_mask2=np.zeros((h,w),np.uint8)
    points2=np.array([[tr2_pt1[0]-x,tr2_pt1[1]-y],[tr2_pt2[0]-x,tr2_pt2[1]-y],
                     [tr2_pt3[0]-x,tr2_pt3[1]-y]],np.int32)
    cv2.fillConvexPoly(cropped_tri_mask2,points2,255)
    cropped_triangle2=cv2.bitwise_and(cropped_triangle2,cropped_triangle2,mask=cropped_tri_mask2)
    #wraping of triangles
    points=np.float32(points)
    points2=np.float32(points2)
    #Matrix for affine transform
    M=cv2.getAffineTransform(points,points2)
    warp_triangle=cv2.warpAffine(cropped_triangle,M,(w,h))
    warp_triangle=cv2.bitwise_and(warp_triangle,warp_triangle,mask=cropped_tri_mask2)
    #Reconstruction of image
    triangle_area=img2_new_face[y:y+h,x:x+w]#this is done to store only previous
    triangle_area_gray=cv2.cvtColor(triangle_area,cv2.COLOR_BGR2GRAY)
    # Let's create a mask to remove the lines between the triangles
    _, line_remove_mask = cv2.threshold(triangle_area_gray,1, 255, cv2.THRESH_BINARY_INV)
    warp_triangle = cv2.bitwise_and(warp_triangle, warp_triangle, mask=line_remove_mask)
    triangle_area=cv2.add(triangle_area,warp_triangle)
    img2_new_face[y:y+h,x:x+w]=triangle_area
    
    

#Face swapped
img2_new_face_gray=cv2.cvtColor(img2_new_face,cv2.COLOR_BGR2GRAY)
#we create a mask of shape img2_new_face to cover on image2 as to extract all part except face 
a,background=cv2.threshold(img2_new_face_gray,1,255,cv2.THRESH_BINARY_INV)
a,bg=cv2.threshold(img2_new_face_gray,1,255,cv2.THRESH_BINARY)
background=cv2.bitwise_and(image2,image2,mask=background)
final=cv2.add(background,img2_new_face)
#seamless cloning to match color of final face with destination image
#center-face2 are the coordinates of center of face,bg is mask ,final is source and image2 is dst
final_face=detector(final)
for face in final_face:
    landmarks=predictor(final,face)
    for i in range(0,68):
        x=landmarks.part(i).x
        y=landmarks.part(i).y
        final_landmark_points.append((x,y))
final_points=np.array(final_landmark_points,np.int32)
final_hull=cv2.convexHull(final_points)
(x,y,w,h)=cv2.boundingRect(final_hull)
center_face2 = (int((x + x + w) / 2), int((y + y + h) / 2))
seamlessclone = cv2.seamlessClone(final, image2,bg, center_face2, cv2.MIXED_CLONE)

cv2.imshow("Image1",image1)
cv2.imshow("Image2",image2)
cv2.imshow("final",final)
cv2.imshow("seamless",seamlessclone)
cv2.waitKey()
cv2.destroyAllWindows()
 
