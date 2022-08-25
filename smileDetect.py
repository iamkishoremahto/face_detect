import cv2
# from faceDetect import *

def cameraCapture():
    
    capture = cv2.VideoCapture(0)
    return capture

def smileDetecting(capture):

    while(capture.isOpened()):

        ret, frame = capture.read()

        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        smileCascade= cv2.CascadeClassifier('haarcascade_smile.xml')
        frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
        faces = faceCascade.detectMultiScale(frameGray,1.1,4)
        drawRectangle(faces=faces,smileCascade=smileCascade,frame=frame,frameGray=frameGray)
        # drawRectangle(faces=smiles,frame=frame)
        if ret:
            cv2.imshow('Video',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def drawRectangle(faces,smileCascade,frame,frameGray):

    for (x,y,width,height) in faces:
        cv2.rectangle(frame, (x,y),(x+width, y+height),(0,255,0),2)
        graySmile = frameGray[y: y + height, x: x + width]
        colorSmile = frameGray[y: y + height, x: x + width]
        smiles = smileCascade.detectMultiScale(graySmile,1.8,4)
        for(sx,sy,sWidth,sHeight) in smiles:
            cv2.rectangle(colorSmile,(sx,sy),(sWidth,sHeight),(255,0,0),2)
    




if __name__ == '__main__':
    
   capture = cameraCapture() 
   smileDetecting(capture=capture)