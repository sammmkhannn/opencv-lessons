import cv2 as cv
import numpy as np

img = cv.imread('./images/sahir.jpeg')
cv.imshow('Sahir', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# laplacion
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacion', lap)

# Sabel
soblex = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobley = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_solbel = cv.bitwise_or(soblex, sobley)
cv.imshow('Soble X', soblex)
cv.imshow('Soble Y', sobley)
cv.imshow('Combined Soble', combined_solbel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
