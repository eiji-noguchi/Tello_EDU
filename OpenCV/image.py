import cv2
import numpy as np
import urllib.request as req #URLを開くための拡張

print("cv2のバージョンは",cv2.__version__)
print("numpyのバージョンは",np.__version__)


# OpenCVでの画像の読み込み
url = "http://uta.pw/gazoubbs/attach/12-hama.jpg"
imageFile = "C:\Drone\Tello_EDU\OpenCV\image\hama.jpg"
# urlの画像を保存先フォルダ（C:\Drone\Tello_EDU\OpenCV\image）にhama.jpgという名前で保存する
# 保存先フォルダは作成してください
req.urlretrieve(url, imageFile)
# 保存した画像ファイルを読み込む
img = cv2.imread(imageFile)
print(img.shape)    # 画像のピクセル、色（RGB）を表示

# グレイスケール（白黒）に変換
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ファイルに保存
cv2.imwrite("C:\Drone\Tello_EDU\OpenCV\image\hama-gray.jpg", gry)