import numpy as np
import cv2
from ImagePrint import image_print

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("RedGerard.mp4")
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
wid = 60

print("\033[2J")

try:
    while(True):
        ret, frame = cap.read()
        image_print(frame, wid)
        print("\033[{}F".format(wid+1))

except KeyboardInterrupt:
    cap.release()
    print("\033[{}E".format(wid+1))


