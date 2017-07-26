import numpy as np
import cv2
cap = cv2.VideoCapture('testvid.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
final_image = np.zeros((400,550,3), np.uint8)
while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    #fgmask = fgbg.apply(frame)
    edges = cv2.Canny(frame,100,200)
    circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=40,minRadius=100,maxRadius=200)
    print(circles)
    newframe = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    #circles = np.uint16(np.around(circles))
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
        	cv2.circle(newframe, (x, y), r, (255, 0, 0), 4)
    cv2.imshow('frame',newframe) 
    out.write(newframe)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
