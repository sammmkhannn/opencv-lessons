import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./images/sahir.jpeg')
cv.imshow('Sahir', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
# grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pexels')
plt.pyplot(gray_hist)
plt.xlim([0, 256])
plt.show()
cv.waitKey(0)
