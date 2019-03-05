import socket

LOCALHOST = '127.0.0.1'
PORT = 7777
BUFFER_SIZE = 2048
local = (LOCALHOST, PORT)

# IPv4,TCPを行うソケットの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    # ソケットを指定したアドレスと結びつける
    # sercerSocket.bind(("",port))にすることでこのマシンが持っている全てのアドレスで接続可能となる
    serverSocket.bind(local)

    # サーバがクライアントからの接続要求を受け入れる用意をする
    # 引数には接続要求を順番待ちさせたい数（通常の最大値）を指定する
    serverSocket.listen(5)

    # 誰か繋がってくれるまで私待ってる
    while True:
        # clientsocketは接続を通じてデータの送受信を行うための新しいソケットオブジェクト
        # addressは接続先でソケットにbindしているアドレス
        clientsocket, address = serverSocket.accept()

        try:
            print("クライアントから接続されました")
            # クライアントからバイト型を受け取る
            data = clientsocket.recv(BUFFER_SIZE)
            print(data.decode())
            # クライアントへ返す
            clientsocket.send(data)
        finally:
            clientsocket.close()