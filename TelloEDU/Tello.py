#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
from msvcrt import getch
from module import jsonKey
import cv2
import numpy as np

host = ''
port = 9000
locaddr = (host,port) 


# UDP通信のためのソケットオブジェクトの生成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

# ソケットを指定したアドレスと結びつける
sock.bind(locaddr)

# Telloからの通信を受け取る
def recv():
    count = 0
    while True: 
        try:
            # Telloからバイト型を受け取る
            # 一度に受信するデータ量は引数で指定する
            data, server = sock.recvfrom(2048)
            res = data.decode(encoding="utf-8")
            print("Telloからの返事",res)

            if(msg == "streamon" and res == "ok"):
                #videoメソッドの呼び出し
                print("カメラスタート")
                video_thread = threading.Thread(target=video())
                video_thread.start()
                           
        except Exception:
            print ('\nExit . . .\n')
            break


# 画像取得処理
def video():     
    # 画像取得処理
    # 顔カスケード取得
    face_cascade = cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    # VideoCapture型のオブジェクトを生成
    cap = cv2.VideoCapture('udp://127.0.0.1:11111')
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

    i = 0
    while(cap.isOpened()): #カメラデバイスが正常にオープンしてるかの確認
        # VideoCaptureから1フレーム読み込む
        # retにはboolが、frameにはフレーム情報が返ってくる
        ret, frame = cap.read()
        frame = cv2.resize(frame, dsize=(720, 480))

        if ret == True:
            i += 1
            # 4フレーム毎に顔認識処理を実行
            if i%25 == 0:
                # 映像をグレー化
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 顔認識
                faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
                if len(faces)>0:
                    # 顔があった場合
                    print("顔認証中")
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
                    # 顔のズーム状況
                    zoom_w = face_w / frame_w
                    zoom_h = face_h / frame_h

                    # 顔の位置によって情報を表示
                    if diff_x > 30:
                        # print("←")
                        move_x = "-30"
                    if diff_x < -30:
                        # print("→")
                        move_x = "30"
                    if diff_y > 30:
                        # print("↑")
                        move_y = "-30"
                    if diff_y < -30:
                        # print("↓")
                        move_y = "30"
                    if zoom_w >= 0.3:
                        # print("顔近い")
                        move_z = "-30"
                    if zoom_h >= 0.3:
                        # print("顔大きい")
                        move_z = "30" 
                    
                    # 指定したxyz軸に移動するコマンドを作成
                    move_speed = "50"
                    move_xyz = "go " + move_x + " " + move_y + " " + move_z + " " + move_speed
                    print(move_xyz)
                    # Telloへ送信
                    sock.sendto(move_xyz.encode(encoding="utf-8"), tello_address)
                    
                for (x,y,w,h) in faces:
                    # 認識している顔に線を引く
                    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                               
                if i > 300:
                    i = 0
            print("顔無し")
                    
            # 画像をウィンドウ上に表示する
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # キャプチャをリリースして、ウィンドウをすべて閉じる
    cap.release()
    cv2.destroyAllWindows()


print ('\r\n\r\nエンターキーで離陸、スペースキーで着陸だよ(/・ω・)/\r\n')

# Telloの操作と受信を並列に処理する
recv_thread = threading.Thread(target=recv)
recv_thread.start()

while True: 

    try:
        # キー入力
        msg = jsonKey.getCommand(getch())

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Telloへ入力されたデータを送る
        sock.sendto(msg.encode(encoding="utf-8"), tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break