import numpy as np
import cv2 as cv

faceCascade = cv.CascadeClassifier('./haar_face.xml')
smileCascade = cv.CascadeClassifier('./haar_smile.xml')
eyeCascade = cv.CascadeClassifier('./haar_eye.xml')

capture = cv.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
while True:
    isTrue, frame = capture.read()
    img = cv.flip(frame, 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=10,
            minSize=(5, 5)
        )

        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=15,
            minSize=(25, 25)
        )

        for (xx, yy, ww, hh) in smile:
            cv.rectangle(roi_color, (xx, yy), (xx+ww, yy+hh), (0, 255, 0), 2)

    cv.imshow('Video', img)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
