from calendar import c
import cv2

def cameraCapture():
    
    capture = cv2.VideoCapture(0)
    return capture

def faceDetecting(capture):

    while(capture.isOpened()):
        ret, frame = capture.read()
        
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(grayFrame,1.1,4)
        drawRectangle(faces=faces, frame=frame)

        if ret:
            cv2.imshow('Video',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def drawRectangle(faces,frame):

    for (x,y,width,height) in faces:
        cv2.rectangle(frame, (x,y),(x+width, y+height),(0,255,0),2)

if __name__ == '__main__':
    capture = cameraCapture()
    faceDetecting(capture=capture)