import cv2 as cv
img = cv.imread('images/sahir.jpeg')
cv.imshow('Sahir', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
# To increase the blurr just increase the krnal size (7,7)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
cany = cv.Canny(img, 125, 175)
cv.imshow('Canny', cany)

# Dialating
dilated = cv.dilate(cany, (3, 3), iterations=1)
cv.imshow('Dialated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)

# Converting an image to grayscale
