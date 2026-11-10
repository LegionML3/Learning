import cv2 as cv

def rescaleFrame(frame, factor=0.75):
    #get the width and hight scaled
    width = int(frame.shape[1] * factor)
    height = int(frame.shape[0] * factor)
    #create a tuple for our new dimensions
    size = (width, height)

    return cv.resize(frame, size, interpolation=cv.INTER_AREA)
