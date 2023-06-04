import cv2 as cv
import numpy as np


img = cv.imread('images/sahir.jpeg')
# cv.imshow('Sahir', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
b, g, r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)
blue = cv.merge([b, blank, blank])
cv.imshow('Blue', blue)
green = cv.merge([blank, g, blank])
cv.imshow('Green', green)
red = cv.merge([blank, blank, r])
cv.imshow('Red', red)


merged = cv.merge([b, g, r])
cv.imshow('MERGE', merged)
cv.waitKey(0)

print(r.shape)
print(g.shape)
print(b.shape)
