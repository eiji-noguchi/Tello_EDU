import socket

LOCALHOST = '127.0.0.1'
PORT = 7777
BUFFER_SIZE = 2048
local = (LOCALHOST, PORT)

# TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    # 引数のアドレスで示されるリモートソケットに接続する
    clientSocket.connect(local)
    data = input("何送る？")
    # 入力値をバイト型に変換し、サーバ側に送る
    clientSocket.send(data.encode())
    recv = clientSocket.recv(BUFFER_SIZE)
    print("サーバから返された",recv.decode())