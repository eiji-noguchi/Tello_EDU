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
#from module import key
from module import jsonKey
import cv2

host = ''
port = 9000
locaddr = (host,port) 


# UDP通信のためのソケットオブジェクトの生成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)
tello_video_port = 11111
# ソケットを指定したアドレスと結びつける
sock.bind(locaddr)

# Telloからの通信を受け取る
def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(2048)
            print("Telloからの返事",data.decode(encoding="utf-8"))

            # 画像取得処理
            # VideoCapture 型のオブジェクトを生成
            cap = cv2.VideoCapture('udp://127.0.0.1:11111')
            while(cap.isOpened()): #カメラデバイスが正常にオープンしてるかの確認
                # VideoCaptureから1フレーム読み込む
                # retにはboolが、frameにはフレーム情報が返ってくる
                ret, frame = cap.read()

                #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 画像をウィンドウ上に表示する
                cv2.imshow('frame',frame)
                
                # qキーでVideoCaptureの終了
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # キャプチャをリリースして、ウィンドウをすべて閉じる
            cap.release()
            cv2.destroyAllWindows()

                    
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nエンターキーで離陸、スペースキーで着陸だよ(/・ω・)/\r\n')


# Telloの操作と受信を並列に処理する
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:
        msg = jsonKey.getCommand(getch())
        print(msg)

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break