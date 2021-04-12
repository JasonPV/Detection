# import the necessary packages
from imutils import face_utils
import imutils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from math import sqrt


def symmetryLines(file):
    # construct the argument parser and parse the arguments
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-p", "--shape-predictor", required=True,
    # help="file")
    #ap.add_argument("-i", "--image", required=True,
    # help="frodo.jpg")
    #args = vars(ap.parse_args())

    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    # load the input image, resize it, and convert it to grayscale
    image = cv2.imread(file)
    image = imutils.resize(image, width=350)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    rects = detector(gray, 1)

    # loop over the face detections
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
    # convert dlib's rectangle to a OpenCV-style bounding box
    # [i.e., (x, y, w, h)], then draw the face bounding box
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # show the face number
    #cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
    # cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    (xl1,yl1)=shape[37]
    (xl2,yl2)=shape[38]
    (xl3,yl3)=shape[40]
    (xl4,yl4)=shape[41]
    cl1 = int(sqrt((xl2-xl1)**2 + (yl2-yl1)**2)/2)
    cl2 = int(sqrt((xl4-xl3)**2 + (yl4-yl3)**2)/2)
    l_start = (xl1+cl1,yl1+cl1)
    l_end = (xl4+cl2,yl4+cl2)
    #cv2.line(image,l_start,l_end,(0, 240, 240),3)
    #print (l_start)
    #k = int((yl1+cl1 - yl4+cl2) / (xl1+cl1 - xl4+cl2))
    #b = yl4+cl2 - k * (xl4+cl2)
    #print(k*203+b)
    # writeln('y = ',k:0:2,'x + ',b:0:2);
    #cv2.line(image, (203,k*203+b), (250, k*250+b), (0,0,0), 2)

    (xf,yf) = shape[8]
    (xs,ys) = shape[27]
    cv2.line(image,(xf,yf),(xs,ys),(0, 240, 240),3)

    #print (xs,ys)
    xl1r = xs - (xl1+cl1)
    xl2 = xf - xl1r
    cv2.line(image,(xl2,yf),(xl1+cl1,ys),(255, 0, 0),3)

    (xr1,yr1)=shape[43]
    (xr2,yr2)=shape[44]
    (xr3,yr3)=shape[46]
    (xr4,yr4)=shape[47]
    cr1 = int(sqrt((xr2-xr1)**2 + (yr2-yr1)**2)/2)
    cr2 = int(sqrt((xr4-xr3)**2 + (yr4-yr3)**2)/2)
    r_start = (xr1+cr1,yr1+cr1)
    r_end = (xr4+cr2,yr4+cr2)
    xr1r = (xr1+cr1) - xs
    xr2 = xf + xr1r
    cv2.line(image,(xr2,yf),(xr1+cr1,ys),(255, 0, 0),3)

    (xrf,yrf) = shape[24]
    (xrs,yrs) = shape[10]
    #cv2.line(image,(xrf,yrf),(xrs,yrs),(255, 0, 0),3)
    (xlf,ylf) = shape[48]
    (xls,yls) = shape[20]
    #cv2.line(image,(xlf,ylf),(xls,yls),(255, 0, 0),3)
    #for (x, y) in leftEye:
    # cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
    #for (x, y) in rightEye:
    # cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
    #for (x, y) in shape:
    #print ((x, y))
    # cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
    return image
    # cv2.imshow('symmetry line', image)
    # cv2.waitKey(0)


if __name__ == '__main__':
    file = 'Эталон.jpg'
    cv2.imshow('symmetry line', symmetryLines(file))
    cv2.waitKey(0)