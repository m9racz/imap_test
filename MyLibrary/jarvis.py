
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
cv2.imshow('image',img)dfd
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
