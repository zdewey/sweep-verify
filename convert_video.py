import numpy as np
import cv2

cap = cv2.VideoCapture('testvid.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1329,484))

mtx = np.array([[886.238, 0., 974.75],
    [0., 893.235, 526.754],
    [0., 0., 1.]])
D = np.array([0., 0., 0., 0.])

while(1):
    ret, frame = cap.read()
    if frame is None:
        continue
    Knew = mtx.copy()
    Knew[(0,1), (0,1)] = 0.4 * Knew[(0,1), (0,1)]
    new_frame = cv2.fisheye.undistortImage(frame, mtx, D=D, Knew=Knew)
    x, y, w, h = [278, 288, 1329, 484]
    new_frame = new_frame[y:y+h, x:x+w]
    out.write(new_frame)
    #cv2.imshow('frame',new_frame) 
cap.release()
out.release()
cv2.destroyAllWindows()
