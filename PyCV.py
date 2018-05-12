import numpy
import cv2
from tkinter import *


# def sizeFiltering(contours):
#     # """
#     # this function filters out the smaller retroreflector (as well as any noise) by size
#     # """
#
#     if len(contours) == 0:
#         print("sizeFiltering: Error, no contours found")
#         return 0
#
#     big = contours[0]
#
#     for c in contours:
#         if type(c) and type(big) == numpy.ndarray:
#             if cv2.contourArea(c) > cv2.contourArea(big):
#                 big = c
#         else:
#             return 0
#     x,y,w,h = cv2.boundingRect(big)
#     #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#     return big

# def biggestContourI(contours):
#     maxVal = 0
#     maxI = None
#     for i in range(0, len(contours) - 1):
#         if len(contours[i]) > maxVal:
#             cs = contours[i]
#             maxVal = len(contours[i])
#             maxI = i
#             x,y,w,h = cv2.boundingRect(biggestContourI(maxI))
#     return maxI

def sortRect(contours):
    largestArea = 200
    for i in range(0, len(contours) - 1):
        area = cv2.contourArea(contours[i])
        if area >largestArea:
            largestArea = area
            x,y,w,h = cv2.boundingRect(contours[i])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


def getWidth(width):
    boxWidth = width/28.39
    return boxWidth

def getHeight(height):
    boxHeight = height/32.4
    return boxHeight

def getArea(w,Height):
    boxArea = getHeight(Height) * getWidth(w)
    return boxArea

def nothing():
 	pass
camera = cv2.VideoCapture(0)
def createGui():
	cv2.namedWindow('test')
	cv2.createTrackbar('upperH', 'test', 50, 255, nothing)
	cv2.createTrackbar('upperS', 'test', 200, 255, nothing)
	cv2.createTrackbar('upperV', 'test', 0, 255, nothing)
	cv2.createTrackbar('lowerH', 'test', 255, 255, nothing)
	cv2.createTrackbar('lowerS', 'test', 255, 255, nothing)
	cv2.createTrackbar('lowerV', 'test', 255, 255, nothing)

createGui()
while True:

    greenLower = (55-cv2.getTrackbarPos('upperH',"test"),cv2.getTrackbarPos("upperS", "test"),cv2.getTrackbarPos("upperv", "test"))
    greenUpper = (55+cv2.getTrackbarPos('UpperH',"test"),cv2.getTrackbarPos('lowerH',"test"),cv2.getTrackbarPos('lowerV',"test"))
    #greenLower = (29, 86, 6)
    #greenUpper = (64, 255, 255)
    (grabbed, frame) = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, greenLower, greenUpper)
    #	mask = cv2.erode(mask, None, iterations=2)
    #	mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        sortRect(cnts)
    	#cv2.circle(frame, (x,y), 20, (0,255,0), thickness=1, lineType=8, shift=0)
    	#cv2.circle(frame, (x+w,y+h), 20, (0,255,0), thickness=1, lineType=8, shift=0)

    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
    	break
camera.release()
cv2.destroyAllWindows()
