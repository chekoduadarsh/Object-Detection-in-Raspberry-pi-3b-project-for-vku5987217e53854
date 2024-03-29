import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#cap = cv2.VideoCapture("placement.mp4")
cap = cv2.VideoCapture(0)   #load video from webcam

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # RGB to Gray conversion
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)     #applay haarcascade

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      #plot rectangle for detected faces
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff          #play video until esc is pressed
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
