import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np

img_origin = cv2.imread('c:\\temp\\marker4.jpg',1)
#img_gray = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)
#img_gray_blur = cv2.medianBlur(img_gray,5)
# Convert BGR to HSV
hsv = cv2.cvtColor(img_origin, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,150,50])
upper_blue = np.array([130,255,255])
# Threshold the HSV image to get only blue colors
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
#odstranit sum
mask_blue_blur = cv2.medianBlur(mask_blue,5)


#find circles
#circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,500,param1=50,param2=100,minRadius=100,maxRadius=0)
#circles = np.uint16(np.around(circles))




#QR = pyzbar.decode(img_gray)
#print(circles[0])


cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)#cv2.WINDOW_AUTOSIZE / WINDOW_NORMAL
cv2.imshow('detected circles',ROI)
cv2.waitKey(0)
cv2.destroyAllWindows()