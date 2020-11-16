import numpy as np
import cv2

cap = cv2.VideoCapture('IMG_1931.MOV')
ground = ""

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ground == "":
    	ground = gray
    else :
    	sub = cv2.subtract(gray, ground)
    	cv2.imshow('frame', sub)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break
    # edges = cv2.Canny(frame,50,100)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cap.release()
cv2.destroyAllWindows()
