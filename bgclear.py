#importing the OpenCV-python module
import cv2 as cv


# if you want you your camera uncomment this and comment the below one
# video = cv.VideoCapture(0)

#this is using the 2.mp4 file which detects the edge of a video
video = cv.VideoCapture('2.mp4')


#below code does all the edging using cv2's createBackgroungSubtractorMOG2 . there will be a detail program of that model . Stay in touch 
clear = cv.createBackgroundSubtractorMOG2(50,20) 

#loop through the video 
while  True:
    

    # read the frame and return r 
    r , frame = video.read()

    if r:
        mask = clear.apply(frame)
        cv.imshow('Mask' , mask)

        if cv.waitKey(5)  == ord('X'):
            break

    else:
        video = cv.VideoCapture('2.mp4')

# we'er clearing the space after program is done

cv.destroyAllWindows() 
video.release()
