import cv2 as cv

img = cv.imread('./images/sahir.jpeg')
cv.imshow('Sahir', img)


# Averaging

average = cv.blur(img, (7, 7))
cv.imshow('Averagin', average)

# Guassion Blur
guass = cv.blur(img, (7, 7), 0)
cv.imshow('Guassion', guass)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
