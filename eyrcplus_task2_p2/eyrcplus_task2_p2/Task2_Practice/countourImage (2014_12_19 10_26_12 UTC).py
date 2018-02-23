'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Functions
*  Filename: contourImage.py
*  Version: 1.0.0  
*  Date: November 3, 2014
*  
*  Author: Arun Mukundan, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
'''

############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image1.png')
cv2.imshow('imgs',img);
#print img.shape
############################################

############################################
## Do the processing
#blur1 = cv2.GaussianBlur(img,(11,35),0)


## for green
param1 = [0,5,0]
param2 = [80,255,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res   = cv2.bitwise_and(img, img, mask= mask)

i =-1
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img,contours,i,(255,0,0),3)
M = cv2.moments(contours[i])
cxg = int(M['m10']/M['m00'])
cyg = int(M['m01']/M['m00'])
#print "Centroid = ", cxg, ", ", cyg
cv2.circle(img,(cxg,cyg), 5, (255,0,0), -1)
#print len(contours)
##for red
for i in range(0,11):
    cv2.line(img,(0,(40*i)),(400,(40*i)),(255,255,255),3)
    cv2.line(img,((40*i) ,0),((40*i) ,400),(255,255,255),3)
blur1 = cv2.GaussianBlur(img,(3,5),0)
param1r = [0,10,0]
param2r = [55,255,255]
hsv = cv2.cvtColor(blur1,cv2.COLOR_BGR2HSV)
lowerr = np.array(param1r)    ## Convert the parameters into a form that OpenCV can understand
upperr = np.array(param2r)
mask  = cv2.inRange(hsv, lowerr, upperr)
resr   = cv2.bitwise_and(blur1, blur1, mask= mask)

i =-1
gray = cv2.cvtColor(resr,cv2.COLOR_BGR2GRAY)
retr,threshr = cv2.threshold(gray,127,255,0)
contoursr, hierarchyr = cv2.findContours(threshr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contoursr,i,(255,255,255),80)
M = cv2.moments(contoursr[i])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#print "Centroid = ", cx, ", ", cy
cv2.circle(img,(cx,cy), 3, (255,0,0), -1)
#print len(contoursr)



##for black
#for i in range(0,11):
  #      cv2.line(img,(0,(40*i)),(400,(40*i)),(255,255,255),3)
   #     cv2.line(img,((40*i) ,0),((40*i) ,400),(255,255,255),3)
blur1 = cv2.GaussianBlur(img,(3,5),0)
param1b = [0,0,0]
param2b = [80,255,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lowerb = np.array(param1b)    ## Convert the parameters into a form that OpenCV can understand
upperb = np.array(param2b)
mask  = cv2.inRange(hsv, lowerb, upperb)
resb   = cv2.bitwise_and(img, img, mask= mask)


gray = cv2.cvtColor(resb,cv2.COLOR_BGR2GRAY)
retb,threshb = cv2.threshold(gray,127,255,0)
contoursb, hierarchyb = cv2.findContours(threshb,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for i in range(1,len(contoursb)):
        #cv2.drawContours(img,contoursb,i,(255,0,0),3)
        M = cv2.moments(contoursb[i])
        cxb = int(M['m10']/M['m00'])
        cyb = int(M['m01']/M['m00'])
        #print "Centroid = ", cx, ", ", cy
        cv2.circle(img,(cxb,cyb), 5, (255,0,0), -1)
print len(contoursb)-1




############################################
## Show the image
##cv2.imshow('image',img)
#cv2.imshow('blur1',blur1)
#cv2.imshow('real',mask);
cv2.imshow('img',img);
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
