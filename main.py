import cv2
import numpy as np
# import imutils
#import time
#import argparse
#import os

cap = cv2.VideoCapture(0)
# cap.set(3,1920)
# cap.set(4,1080)
# cap.set(10,2)
cap.set(5, 30)

while (1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !
    lower_white = np.array([0, 0, 230], dtype=np.uint8)
    upper_white = np.array([180, 25, 255], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts2 = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts3 = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cnts = cnts[]
    # cnts = cnts0[0] if cap.read() else cnts0[1]
    # cnts2 = cnts[0] if cap.read() else cnts[1]
    # cnts3 = cnts[0] if cap.read() else cnts[1]
    center = None
    # center2 = None
    # center3 = None

    # only proceed if at least one contour was found
    # if len(cnts0) > 0:
    # find the largest contour in the mask, then use
    # it to compute the minimum enclosing circle and
    # centroid
    # c0 = max(cnts0, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(cnts)
    M = cv2.moments(cnts)
    center0 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    # если изменить последний M0 на M то можно попробовать измерить глубину

    # only proceed if the radius meets a minimum size
    # if radius0 > 1:
    # draw the circle and centroid on the frame,
    # then update the list of tracked points
    cv2.circle(res, (int(x), int(y)), int(radius), (0, 255, 255), 2)
    cv2.circle(res, center, 5, (0, 0, 255), -1)

    # cnts1 = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts1 = cnts1[0] if cap.read() else cnts1[1]
    # center1 = None

    # if len(cnts1) > 0 :
    # find the largest contour in the mask, then use
    # it to compute the minimum enclosing circle and
    # centroid
    # c1 = max(cnts1, key=cv2.contourArea)
    # ((x1, y1), radius1) = cv2.minEnclosingCircle(c1)
    # M1 = cv2.moments(c1)
    # center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))
    # если изменить последний M0 на M то можно попробовать измерить глубину

    # only proceed if the radius meets a minimum size
    # if radius1 > 1:
    # draw the circle and centroid on the frame,
    # then update the list of tracked points
    # cv2.circle(res, (int(x1), int(y1)), int(radius1), (0, 255, 255), 2)
    # cv2.circle(res, center1, 5, (0, 0, 255), -1)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # show the frame to our screen
    # cv2.imshow("Frame", frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
# vs.stop()