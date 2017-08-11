import numpy as np
import cv2
import math
cap = cv2.VideoCapture('testvid.mp4')

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
final_image = np.zeros((400,550,3), np.uint8)
while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    #fgmask = fgbg.apply(frame)
    edges = cv2.Canny(frame,100,200)
    circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=12,maxRadius=20)
    circles2 = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=5,maxRadius=13)
    print(circles)
    newframe = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    #circles = np.uint16(np.around(circles))s
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
                cv2.circle(newframe, (x, y), r, (255, 0, 0), 4)
                cv2.circle(newframe, (x, y), 2, (255, 0, 0), 3)
        if circles2 is not None:
            circles2 = np.round(circles2[0, :]).astype("int")
            for (x, y, r) in circles:
                for (x2, y2, r2) in circles2:
                    distance = math.sqrt(math.pow((x-x2),2) + math.pow((y-y2),2))
                    #print(distance)
                    if distance > 45 and distance < 60:
                        cv2.line(newframe, (x, y), (x2, y2), (255, 0, 255), 3)
    if circles2 is not None:
        #circles2 = np.round(circles2[0, :]).astype("int")
        for (x, y, r) in circles2:
                cv2.circle(newframe, (x, y), r, (0, 0, 255), 3)
                cv2.circle(newframe, (x, y), 2, (0, 0, 255), 2)
    cv2.imshow('frame',newframe) 
    #out.write(newframe)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
#out.release()
cv2.destroyAllWindows()
