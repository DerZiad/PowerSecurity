import numpy as np
import cv2
import os

namefolder = str(input("Enter the name of the person => : "))
os.mkdir(namefolder)

speech("S'il vous plait " + namefolder + ", montrez moi votre visage sans lunette : ",lang="fr",slow=True)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
i = 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in faces:
        #roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        color = (255,0,0)
        stroke = 2
        width = x +  w
        heigth= y + h
        savePath = namefolder + "/" + str(i) + ".png"
        cv2.imwrite(savePath, roi_color)
        cv2.rectangle(frame,(x,y),(width,heigth),color,stroke)
        i = i + 1
    if i == 500:
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()