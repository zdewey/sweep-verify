import numpy as np
import cv2
cap = cv2.VideoCapture('testvid.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    #fgmask = fgbg.apply(frame)
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('frame',edges) 
    out.write(edges)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
