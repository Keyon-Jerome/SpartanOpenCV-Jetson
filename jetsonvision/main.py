import cv2
import numpy as np
# https://docs.opencv.org/3.3.1/d4/d73/tutorial_py_contours_begin.html
cap = cv2.VideoCapture(0)


while True:

    # Take each frame
    _, frame = cap.read()

    # blur the frame so the cube is more complete
    blurred_frame =cv2.blur(frame,(5,5))
    blurred_frame = cv2.medianBlur(blurred_frame,5)
    
    # Convert BGR (RGB) to HSV coloring
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # define range of yellow color in HSV
    lower_yellow = np.array([20,50,50])
    upper_yellow = np.array([50,255,255])

    # exact power up cube cube color
    cube_color = np.array([56,54,89])
    
    # Threshold the HSV image to get only power cube colors;
    # only colors between lower_yellow and upper_yellow
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Bitwise-AND mask and original image
    # don't know what this means lol
    # res = cv2.bitwise_and(frame,frame, mask= mask)

    # show all three windows
    #cv2.imshow('frame',frame)
    #cv2.imshow('res',res)
    
    testImage = cv2.imread("powerupcube3.jpg")
    blurredTestImage = cv2.blur(testImage,(5,5))
    hsvtest = cv2.cvtColor(blurredTestImage,cv2.COLOR_BGR2HSV)
    testMask = cv2.inRange(hsvtest,lower_yellow,upper_yellow)
    _,testContours,_ = cv2.findContours(testMask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(testMask,testContours,-1,(90,0,0),2)
    cv2.imshow("test",testMask)
    
    initial_mask, contours, hierarchy =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(mask, contours, -1, (90,0,0), 2)
        
    cv2.imshow('mask',mask)
    # if Esc is pressed, terminate program. & is a bitwise operator
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
# stop video capture, then close all windows (end program)
cap.release()
cv2.destroyAllWindows()
