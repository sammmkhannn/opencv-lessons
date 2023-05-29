import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
# img = cv.imread('./sahir.jpeg')
# cv.imshow('Blank', blank)
# 1. paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)
# cv.rectangle(blank, (0, 250), (250, 250),
#              (255, 255, 255), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)
# cv.rectangle(blank, (0, 250), (500, 500),
#              (255, 0, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# cv.rectangle(blank, (250, 0), (500, 250),
#              (255, 255, 255), thickness=cv.FILLED)
# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2,
#           blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)

# # 4. Draw a line
# cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)
# cv.line(blank, (250, 250), (500, 255), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)
# cv.line(blank, (250, 250), (0, 500), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# 4. Write text on image
cv.putText(blank, 'Hello there', (0, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
