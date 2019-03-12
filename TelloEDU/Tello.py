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
    # VideoCapture型のオブジェクトを生成
    cap = cv2.VideoCapture('udp://127.0.0.1:11111')
    while(cap.isOpened()): #カメラデバイスが正常にオープンしてるかの確認
        # VideoCaptureから1フレーム読み込む
        # retにはboolが、frameにはフレーム情報が返ってくる
        ret, frame = cap.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 画像をウィンドウ上に表示する
        cv2.imshow('Tello',frame)
        
        # qキーでVideoCaptureの終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
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
        msg = jsonKey.getCommand(getch())
        print(msg)

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Telloへ入力されたデータを送る
        sent = sock.sendto(msg.encode(encoding="utf-8"), tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break