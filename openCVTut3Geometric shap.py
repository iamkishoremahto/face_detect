import cv2


def cameraCapture():
    capture = cv2.VideoCapture(0)
    return capture
    
def motionDetect(capture):

    while (capture.isOpened()):
        ret, frame1 = capture.read()
        ret, frame2 = capture.read()
        frame1,contours = contoursFinder(frame1,frame2)
        rectangleOnFrame(frame1=frame1,contours=contours)
        # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
        if ret:
            cv2.imshow("video",frame1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    capture.release()
    cv2.destroyAllWindows()

def contoursFinder(frame1,frame2):

    differenceBetweenFrame = cv2.absdiff(frame1,frame2)
    gryaScaleFrame = cv2.cvtColor(differenceBetweenFrame,cv2.COLOR_BGR2GRAY)
    blurGrayScaleFrame = cv2.GaussianBlur(gryaScaleFrame,(5,5),0)
    _,thresholdFrame = cv2.threshold(blurGrayScaleFrame,20,255,cv2.THRESH_BINARY)
    dilatedFrame = cv2.dilate(thresholdFrame,None,iterations=3)
    contours,_ = cv2.findContours(dilatedFrame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return frame1,contours

def rectangleOnFrame(contours,frame1):
    
    for contour in contours:
        (x,y,width,height) = cv2.boundingRect(contour)
        if cv2.contourArea(contour)<700:
            continue
        else:
            # cv2.rectangle(frame1,(x,y),(x+width,y+height),(0,255,0),2)
            cv2.putText(frame1,"Status: Movement ",(20,30),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=(0,0,255),thickness=2)
    


if __name__ == '__main__':
    capture = cameraCapture()
    motionDetect(capture)
    

