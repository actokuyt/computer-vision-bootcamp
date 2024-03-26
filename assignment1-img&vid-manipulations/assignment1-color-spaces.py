import cv2 as cv
import numpy as np


sensitivity = 10
image = cv.imread("bgr.jpg")
video = cv.VideoCapture("bgr.mp4")
input_source = input("What do you want to use as input, image?, video? or cam-feed?:")

def bgr2hsv_range (bgr_color):
    color = np.uint8([[bgr_color]])
    hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    return hsv_color


# define hsv values to track
# blue
lower_blue = np.array([bgr2hsv_range([255,0,0])[0][0][0] - sensitivity,50,50])
upper_blue = np.array([bgr2hsv_range([255,0,0])[0][0][0] + sensitivity,255,255])
# green 
lower_green = np.array([bgr2hsv_range([0,255,0])[0][0][0] - sensitivity,50,50])
upper_green = np.array([bgr2hsv_range([0,255,0])[0][0][0] + sensitivity,255,255])
# red
lower_red = np.array([bgr2hsv_range([0,0,255])[0][0][0] - sensitivity,50,50])
upper_red = np.array([bgr2hsv_range([0,0,255])[0][0][0] + sensitivity,255,255])



# Track Using Images
if input_source == "image" :
    resized_image = cv.resize(image, (200,200))
    image_hsv = cv.cvtColor(resized_image, cv.COLOR_BGR2HSV)
    mask_green = cv.inRange(image_hsv, lower_green, upper_green)
    mask_blue = cv.inRange(image_hsv, lower_blue, upper_blue)
    mask_red = cv.inRange(image_hsv, lower_red, upper_red)
    res_green = cv.bitwise_and(resized_image,resized_image, mask= mask_green)
    res_red = cv.bitwise_and(resized_image,resized_image, mask= mask_red)
    res_blue = cv.bitwise_and(resized_image,resized_image, mask= mask_blue)
    res_combined = cv.add(cv.add(res_blue, res_green), res_red)
    cv.imshow('Original',resized_image)
    cv.imshow('Red Tracked',res_red)
    cv.imshow('Green Tracked',res_green)
    cv.imshow('Blue Tracked',res_blue)
    cv.imshow('Combined',res_combined)
    k = cv.waitKey(0) & 0xFF

    if k == 115:
        cv.imwrite('original.jpg',resized_image)
        cv.imwrite('red-tracked.jpg',res_red)
        cv.imwrite('greentracked.jpg',res_green)
        cv.imwrite('bluetracked.jpg',res_blue)
        cv.imwrite('combined.jpg',res_combined)


    cv.destroyAllWindows()


# Track Using Videos
elif input_source == "video" :

    while True:
        _, frame = video.read()
        resized_image = cv.resize(frame, (400,200))
        image_hsv = cv.cvtColor(resized_image, cv.COLOR_BGR2HSV)
        mask_green = cv.inRange(image_hsv, lower_green, upper_green)
        mask_blue = cv.inRange(image_hsv, lower_blue, upper_blue)
        mask_red = cv.inRange(image_hsv, lower_red, upper_red)
        res_green = cv.bitwise_and(resized_image,resized_image, mask= mask_green)
        res_red = cv.bitwise_and(resized_image,resized_image, mask= mask_red)
        res_blue = cv.bitwise_and(resized_image,resized_image, mask= mask_blue)
        res_combined = cv.add(cv.add(res_blue, res_green), res_red)
        cv.imshow('Original',resized_image)
        cv.imshow('Red Tracked',res_red)
        cv.imshow('Green Tracked',res_green)
        cv.imshow('Blue Tracked',res_blue)
        cv.imshow('Combined',res_combined)
        k = cv.waitKey(5) & 0xFF

        if k == 27:
            break
    video.release()
    cv.destroyAllWindows()


# Track using a cam feed
elif input_source == "cam-feed":
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
 
    while True:
    
        # Take each frame
        _, frame = cap.read()
        
        resized_frame = cv.resize(frame, (400, 200))
    
        # Convert BGR to HSV
        hsv = cv.cvtColor(resized_frame, cv.COLOR_BGR2HSV)
    
        # Threshold the HSV image to get only blue colors
        mask_green = cv.inRange(hsv, lower_green, upper_green)
        mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
        mask_red = cv.inRange(hsv, lower_red, upper_red)
    
        # Bitwise-AND mask and original image
        res_green = cv.bitwise_and(resized_frame,resized_frame, mask= mask_green)
        res_red = cv.bitwise_and(resized_frame,resized_frame, mask= mask_red)
        res_blue = cv.bitwise_and(resized_frame,resized_frame, mask= mask_blue)

        # merge tracking results to one frame
        res_combined = cv.add(cv.add(res_blue, res_green), res_red)
 
        # display results
        cv.imshow('Original',resized_frame)
        cv.imshow('Red Tracked',res_red)
        cv.imshow('Green Tracked',res_green)
        cv.imshow('Blue Tracked',res_blue)
        cv.imshow('Combined',res_combined)

        # save and break if 's' is pressed or break if esc is pressed
        k = cv.waitKey(5) & 0xFF

        if k == 27:
            break
    cap.release()
    cv.destroyAllWindows()