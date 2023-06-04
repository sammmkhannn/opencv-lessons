import os
import cv2 as cv
import numpy as np


DIR = './lfw_funneled'
haar_cascade = cv.CascadeClassifier('./haar_face.xml')

people = []
features = []
labels = []


def create_train():
    for item in os.listdir(DIR)[:10]:
        path = os.path.join(DIR, item)
        people.append(item)
        labels.append(people.index(item))

        # traverse the images

        for image in os.listdir(path):
            img_path = os.path.join(path, image)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)


create_train()
print('Training Done ---------------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and the labels list
face_recognizer.train(features, labels)

np.save('features.npy', features)
np.save('labels.npy', labels)
