import cv2 as cv
import rescale

#image capture
raw_img = cv.imread(r'vision\imgs\cat_imgs\25_1.jpg')

scaled_img = rescale.rescaleFrame(raw_img, 3)

cv.imshow('Scaled Cat', scaled_img)
cv.waitKey(0)

#video capture
capture = cv.VideoCapture(r'vision\vids\cat_vid.mp4')

while True:
    #get
    isTrue, raw_frame = capture.read()
    # check if break
    if cv.waitKey(20) % 0xFF == ord('d') or raw_frame is None:
        break
    #process
    scaled_frame = rescale.rescaleFrame(raw_frame, 1.4)
    #show
    cv.imshow('Cat Video', scaled_frame)
