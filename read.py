import cv2 as cv
# img = cv.imread('./images/sahir.jpeg')
# cv.imshow('sam', img)

# reading videos

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()