import cv2
import numpy as np

print("cv2のバージョンは",cv2.__version__)
print("numpyのバージョンは",np.__version__)


# OpenCVでの画像の読み込み
import urllib.request as req #URLを開くための拡張
url = "http://uta.pw/gazoubbs/attach/12-hama.jpg"
imageFile = "C:\Drone\Tello_EDU\OpenCV\image\hama.jpg"
req.urlretrieve(url, imageFile)
img = cv2.imread(imageFile)
print(img.shape)    # 画像のピクセル、色（RGB）を表示

# 白黒画像に変換
# グレイスケールに変換
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ファイルに保存
cv2.imwrite("C:\Drone\Tello_EDU\OpenCV\image\hama-gray.jpg", gry)