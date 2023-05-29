import cv2 as cv
import numpy as np

img = cv.imread('images/sahir.jpeg')

# cv.imshow('sahir', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur the image

blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.imshow('Thresh', thresh)
print(f'{len(contours)} found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Countours Drawn', blank)
cv.waitKey(0)
