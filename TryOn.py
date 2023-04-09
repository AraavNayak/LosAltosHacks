import cv2
import  cvzone
import numpy as np
from PILasOPENCV import Image

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
num=1

while True:
    k=cv2.waitKey(1)
    if k==ord('s'):
        num=num+1 
    if(num<=10):
        overlay = cv2.imread('Glasses/{}.png'.format(num), cv2.IMREAD_UNCHANGED)
         
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        overlay_resize = cv2.resize(overlay,(int(0.8 * w),int(0.8 * (h*0.6))))
        try:
            frame = cvzone.overlayPNG(frame, overlay_resize, [x + 40, y + 75])
        except ValueError:
            frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
    cv2.imshow('SnapLens', frame)
    if cv2.waitKey(10) == ord('q'):
        break
    if(num>10):
        num=1
  
cap.release()
cv2.destroyAllWindows()
