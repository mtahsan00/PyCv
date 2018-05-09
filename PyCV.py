import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('hellWorld.avi', fourcc, 20.0, (640,480))
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)
    lower_hsv = np.array([50,200,0])
    upper_hsv = np.array([255,255,255])
    mask = cv2.inRange(hsv, lower_hsv,upper_hsv)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    #out.write(frame)
#    cv2.line(cap, (0,0),(150,150), (0,0,0))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()
