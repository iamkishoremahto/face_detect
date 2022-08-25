import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(True):


    ret , frame = capture.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video Camera',gray)
        output.write(frame)
        # key = cv2.waitKey()
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
capture.release()
output.release()
cv2.destroyAllWindows()