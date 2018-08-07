'''
#import jarvis2
import sele

#SD = jarvis2.SpeechDetector()
#SD.run()



web = sele.webcontrol()
web.play_music()
'''



import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np

img_origin = cv2.imread('c:\\temp\\marker2a.jpg',1)
gray = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(gray,5)
#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cimg = img_origin



circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,500,param1=50,param2=100,minRadius=100,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    circle = (i[0],i[1])
    circle_radius = i[2]
    circle_x = i[0]
    circle_y = i[1]


height, width, channels = cimg.shape

delta_x = circle_x - (width/2)
delta_y = circle_y - (height/2)
font = cv2.FONT_HERSHEY_SIMPLEX
text_x = 'deltaX = ' + str(delta_x) + 'px'
text_y = 'deltaY = ' + str(delta_y) + 'px'
cv2.putText(cimg,text_x,(10,500), font, 3,(255,0,0),4,cv2.LINE_AA)
cv2.putText(cimg,text_y,(10,600), font, 3,(255,0,0),4,cv2.LINE_AA)

cv2.line(cimg,(width/2,0),((width/2),height),(0,0,255),2)
cv2.line(cimg,(0,height/2),(width,height/2),(0,0,255),2)


# Build mask
mask = np.zeros(cimg.shape, dtype=np.uint8)
cv2.circle(mask, circle, circle_radius, (255, 255, 255), -1, 8, 0)

# Apply mask (using bitwise & operator)
ROI = cimg & mask

# Crop/center result (assuming max_loc is of the form (x, y))
ROI = ROI[circle[1] - circle_radius:circle[1] + circle_radius,
                            circle[0] - circle_radius:circle[0] + circle_radius, :]

QR = pyzbar.decode(ROI)
text_ID = 'ID: ' + str(QR[0][0])
cv2.putText(cimg,text_ID,(10,400), font, 3,(255,0,0),4,cv2.LINE_AA)

'''
 for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
'''
#print(ROI.shape)

cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)#cv2.WINDOW_AUTOSIZE
#cv2.imshow('detected circles',ROI)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()




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

    laplacian = cv2.Laplacian(gray,cv2.CV_64F)
    #edges = cv2.Canny(gray,100,200)
    #cv2.rectangle(gray,(384,0),(510,128),(200),3)

    # Display the resulting frame
    cv2.imshow('frame',frame)
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
