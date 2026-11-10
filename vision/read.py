import cv2 as cv

img = cv.imread(r'vision\images\25_1.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)