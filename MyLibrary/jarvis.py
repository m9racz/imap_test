'''
import cv2
import numpy as np

img = cv2.imread('c:\\temp\\marker2.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)



circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,500,param1=50,param2=100,minRadius=200,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)#cv2.WINDOW_AUTOSIZE
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



'''
#run video stream in grey

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #laplacian = cv2.Laplacian(gray,cv2.CV_64F)
    #edges = cv2.Canny(gray,100,200)
    #cv2.rectangle(gray,(384,0),(510,128),(200),3)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''






#show picture (matplotlib BGR -> RGB...)
'''
import numpy
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('c:\\temp\\hulky.jpeg',1)


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
'''

'''
cv2.namedWindow('image', cv2.WINDOW_NORMAL)#cv2.WINDOW_AUTOSIZE
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
