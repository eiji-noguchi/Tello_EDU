# Tello EDUをPythonで動かしてみよう

##  まずはPythonをインストール
[Pythonホームページ](https://www.python.org/downloads/)から対応するものをインストールしよう('ω')ノ
[インストール参考サイト](https://www.python.jp/install/windows/install_py3.html)

インストール後コマンドプロンプトで書きコマンドを入力し、インストールしたPythonのバージョンが返ってくることを確認する。
```
$ python -V
```
##  pythonを動かしてみよう
Pythonをインストールしたディレクトリに適当なテキストエディターで
```python
print("Hello,Python")
```
と書かれたファイルを用意し、拡張子を.pyにして保存。
※デフォルトではここにあるかも
- C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.x

コマンドプロンプトのディレクトリをPythonをインストールした直下に移動し、以下コマンドでPythonファイルを実行してみる。
```
$ python <ファイル名>.py
```
これで`Hello,Python`って返事が来たらOK。

##  セットアップ
- [Tello SDK2.0 User Guide](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)を取得する
- 先ほどと同様にPythonをインストールしたフォルダに[公式サンプルコード](https://dl-cdn.ryzerobotics.com/downloads/tello/20180222/Tello3.py)を置く。
- Telloの電源を入れ、PCからTelloのWifiアクセスポイントへ繋ぐ。(SSIDは[TELLO-XXXX])
- TelloのIPは192.168.10.1なのでpingで接続確認を行う。

```
$ ping 192.168.10.1
```
通信の確認が取れたらコマンドプロンプトから先ほどのサンプルコードを実行する。以下のように表示されればOK。

```
$ python Tello3.py

Tello Python3 Demo.

Tello: command takeoff land flip forward back left right
       up down cw ccw speed speed?

end -- quit demo.
```
後は先ほどのUser Guideに記載のTello Commandsより操作したいコマンドを入力する。
例えば、`command`と入力すればTelloとの通信が確認できる。`takeoff`では離陸が、`land`と入力すれば着陸ができる。
サンプルコードの実行を終了させるには`end`を入力すればよい。
