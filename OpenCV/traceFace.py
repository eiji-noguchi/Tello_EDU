import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# 幅
frame_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# 高さ
frame_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 総フレーム数
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# fps
fps = cap.get(cv2.CAP_PROP_FPS)
print(frame_w)
print(frame_h)
print(count)
print(fps)


# 顔の位置座標
face_x = None
face_y = None
face_w = None
face_y = None

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces)>0:
            face_x = faces[0][0]
            face_y = faces[0][1]
            face_w = faces[0][2]
            face_h = faces[0][3]

            # 顔の中心座標を取得
            face_center_x = face_x + face_w/2
            face_center_y = face_y + face_h/2
            # フレームの中心座標を取得
            frame_center_x = frame_w/2
            frame_center_y = frame_h/2
            # フレームの中心と顔の中心座標の差を取得
            diff_x = frame_center_x - face_center_x
            diff_y = frame_center_y - face_center_y

            if diff_x > 30:
                print("👈")
            if diff_x < -30:
                print("👉")
            if diff_y > 30:
                print("👆")
            if diff_y < -30:
                print("👇")
        
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()