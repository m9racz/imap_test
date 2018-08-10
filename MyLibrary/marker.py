import numpy as np
import pyzbar.pyzbar as pyzbar
import cv2


font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = cv2.imread('c:\\temp\\marker_bar.jpg',1)
    delta_x = None
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,500,param1=50,param2=100,minRadius=90,maxRadius=0)
    
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

            height, width, channels = frame.shape
            delta_x = i[0] - (width/2)
            delta_y = i[1] - (height/2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_x = 'deltaX: ' + str(delta_x) + 'px'
            text_y = 'deltaY: ' + str(delta_y) + 'px'


            mask = np.zeros(frame.shape, dtype=np.uint8)
            cv2.circle(mask, (i[0],i[1]), i[2], (255, 255, 255), -1, 8, 0)
            # Apply mask (using bitwise & operator)
            ROI = frame & mask
            # Crop/center result (assuming max_loc is of the form (x, y))
            ROI = ROI[i[1] - i[2]:i[1] + i[2],
                            i[0] - i[2]:i[0] + i[2], :]
            #cv2.imwrite('c:\\temp\\ROI_edges.jpg',ROI)
            ROI_gray = cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)
            ROI_edges = cv2.Canny(ROI_gray,50,150,apertureSize = 3)
            lines = cv2.HoughLines(ROI_edges,1,np.pi/180,100)
            try:
                for rho,theta in lines[0]:
                    angle = ((180/np.pi)*theta)-180
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))
                    x1 = x1 + i[0]-i[2]
                    y1 = y1 + i[1]-i[2]
                    x2 = x2 + i[0]-i[2]
                    y2 = y2 + i[0]-i[2]
                    cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
                    text_angle = 'uhel: ' + str(round(angle))
                    print("uhel")
                    print(angle)
                    
            except:
                text_angle = 'uhel: ???'
            cv2.putText(frame,text_angle,(10,180), font, 1,(255,0,0),2,cv2.LINE_AA)
            cv2.putText(frame,text_x,(10,60), font, 1,(255,0,0),2,cv2.LINE_AA)
            cv2.putText(frame,text_y,(10,120), font, 1,(255,0,0),2,cv2.LINE_AA)
            cv2.line(frame,(width/2,0),((width/2),height),(0,0,255),2)
            cv2.line(frame,(0,height/2),(width,height/2),(0,0,255),2)

            break
    except:
        pass
    # Display the resulting frame

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)#cv2.WINDOW_AUTOSIZE / WINDOW_NORMAL
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()