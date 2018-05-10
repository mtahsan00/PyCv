

from collections import deque
import numpy as np
import cv2


greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

camera = cv2.VideoCapture(0)


while True:

	(grabbed, frame) = camera.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	if len(cnts) > 0:
	

		c = max(cnts, key=cv2.contourArea)
		x,y,w,h = cv2.boundingRect(c)

		if True:

			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)




	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF


	if key == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
