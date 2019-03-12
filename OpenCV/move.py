import cv2
import numpy as np

# VideoCapture 型のオブジェクトを生成
# 引数にはPCに接続されているカメラのデバイス番号（PC内蔵カメラの場合は0）か読み込みたい動画ファイルのファイル名を指定
# 1フレームごとに撮影することが可能
#cap = cv2.VideoCapture('C:\Drone\Tello_EDU\OpenCV\image\move.MOV')
cap = cv2.VideoCapture(0)

#録画用データフォーマットを一意に識別するための4バイトの並びを指定??
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# VideoWriter 型のオブジェクトを生成
# 第一引数：保存ファイル名、第二引数：FourCCコード??、第三引数：フレームレート、第四引数：カラーフラグ??
writer = cv2.VideoWriter('OpenCV/Record/ROKUGA.avi',fourcc,30.0,(640,480))

while(cap.isOpened()): #ビデオキャプチャが正常にオープンしているかの確認
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    #カメラが撮れてたら録画する
    if ret == True:
        #frameの書き出し
        writer.write(frame)

        # 画像をウィンドウ上に表示する
        cv2.imshow('frame',frame)
        # 指定された時間(ms)だけキーボード入力を受け付ける
        # 指定時間が長いと動画はスローになる。また0を指定した場合は何かしらのキーを打つまでキー入力を無期限で待
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
writer.release()
cv2.destroyAllWindows()