# plot photo with detected faces using opencv cascade classifier
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
import imutils
import matplotlib.pyplot as plt


def viola_jones(path):
    # load the photograph
    pixels = imread(path)
    pixels = imutils.resize(pixels, width=350)
    # load the pre-trained model
    classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
    # perform face detection
    bboxes = classifier.detectMultiScale(pixels)
    # print bounding box for each detected face
    for box in bboxes:
        # extract
        x, y, width, height = box
        x2, y2 = x + width, y + height
        # draw a rectangle over the pixels
        rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
    # show the image
    return pixels
    # imshow('face detection', pixels)
    # while True:
    #     k = waitKey(0) & 0xFF
    #     if k == 27:
    #         destroyAllWindows()
    #         break



if __name__ == '__main__':
    path = 'test.jpg'
    viola_jones(path)