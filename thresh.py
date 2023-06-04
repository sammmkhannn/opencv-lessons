import cv2 as cv

img = cv.imread('images/sahir.jpeg')
cv.imshow('Sahir', img)

gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

# inverse thresholding
threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding inverse', thresh_inverse)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)
cv.waitKey(0)
