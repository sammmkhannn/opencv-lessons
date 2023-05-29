import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/FfNmgEUXgAIuV52 (1).jpeg')
# cv.imshow('Home', img)

# plt.imshow(img)
# plt.show()
# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HST2BGR', hsv_bgr)
# plt.imshow(rgb)
# plt.show()
cv.waitKey(0)
