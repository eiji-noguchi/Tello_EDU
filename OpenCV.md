# OpenCVを使ってみよう
## pipが対応しているcpの確認

まずpipのバージョンを確認する。コマンドプロンプトで以下コマンドを入力する。
```
pip -V
```
pip10.0.1以上であればPython上で以下を実行
```Python
from pip._internal.pep425tags import get_supported
get_supported()
```
## pipに対応している.whlファイルをインストールする

[参考サイト](https://qiita.com/kenta1984/items/16a14f3bfaf1f257c585)
