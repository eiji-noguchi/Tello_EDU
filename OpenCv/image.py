import cv2
import numpy as np

cap = cv2.VideoCapture('C:\Drone\Tello_EDU\OpenCv\image\move.MOV')

while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('����',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()