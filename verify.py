import numpy as np
import cv2
cap = cv2.VideoCapture('testvid.mp4')

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720))

#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
final_image = cv2.imread('bg.png')
final_nobg = np.zeros((484,1328,3), np.uint8)
while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    #fgmask = fgbg.apply(frame)
    edges = cv2.Canny(frame,100,200)
    circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=12,maxRadius=20)
    backcircle = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minradius=5,maxRadius=8)
    print(circles)
    newframe = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    #circles = np.uint16(np.around(circles))
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(newframe, (x, y), r, (255, 0, 0), 4)
            cv2.circle(final_image, (x,y), 28, (255, 0, 0), -1)
            cv2.circle(final_nobg, (x,y), 28, (255, 0, 0), -1)
    cv2.imshow('frame',final_image)
    cv2.imshow('frame2',newframe)
    #out.write(newframe)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

x, y, w, h = [434, 28, 375, 375]
final_nobg = final_nobg[y:y+h, x:x+w]
count = cv2.cvtColor(final_nobg, cv2.COLOR_BGR2GRAY)
print((np.count_nonzero(final_nobg))/127787)
cv2.imwrite('result.png',final_image)
cap.release()
out.release()
cv2.destroyAllWindows()
