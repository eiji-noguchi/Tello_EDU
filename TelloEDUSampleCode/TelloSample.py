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


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

#socketをlocaddrにバインドする
sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)  #Telloからデータを受け取る
            print("data",data)
            print("server",server)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')

"""
recvThread create
socketとのやり取りを並列処理にする
"""
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:
        #入力されたコマンドを格納
        msg = input("")

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        #データをsocketに送信
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address) 
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




