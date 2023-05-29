import cv2 as cv

# img = cv.imread('./images/sahir.jpeg')
# cv.imshow('sam', img)


def rescaleFrame(frame, scale=0.75):
    # this will work for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # only works for live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    shortened = rescaleFrame(frame)
    cv.imshow('Video', shortened)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
