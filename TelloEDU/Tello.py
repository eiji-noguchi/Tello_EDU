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


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)
tello_video_port = 11111

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(2048)
            print("Telloからの返事",data.decode(encoding="utf-8"))
            print("data",data)
            print("server",server)

            # 画像取得処理
            cap = cv2.VideoCapture('udp://127.0.0.1:11111')
            while(cap.isOpened()):
                ret, frame = cap.read()

                #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                cv2.imshow('frame',frame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

                    
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nスペースキーで離着陸できるよ(/・ω・)/\r\n')



#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


while True: 

    try:
        #msg = key.getCommand(getch())
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