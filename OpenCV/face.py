import numpy as np
import cv2
import os
import time

# https://github.com/opencv/opencv/tree/master/data/haarcascadesから街頭のファイルを取得しておく
face_cascade = cv2.CascadeClassifier('Tello_EDU\OpenCV\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Tello_EDU\OpenCV\haarcascade_eye.xml')

filePath = os.path.join("C:\\","Drone","photo","abe.jpg")
img = cv2.imread(filePath)
# 多分カラーだと処理が重くなるから一旦白黒にしている
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''顔を認識する
detectMultiScale(
        image:ここに格納されている画像が対象になる
        scaleFactor:画像スケールにおける縮小量
        minNeighbors:物体候補となる矩形は、最低でもこの数だけの近傍矩形を含む必要がある
)
'''
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)
for (x,y,w,h) in faces:
    # 画像に線を描く 
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # 目を認識
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()