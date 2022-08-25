import cv2
# from faceDetect import *

def Cascade():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    return faceCascade, smileCascade

def gray(frame):
    return cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

def detect(grayFrame,faceCascade,smileCascade):
    



if __name__ == '__main__':
    capture = cv2.VideoCapture(0)

    while(capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            grayFrame = gray(frame=frame)

