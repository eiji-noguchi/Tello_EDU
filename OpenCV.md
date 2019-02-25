# OpenCVを使ってみよう
## pipが対応しているcpの確認

まずpipのバージョンを確認する。コマンドプロンプトで以下コマンドを入力する。
```
pip -V
```
pip10.0.1以上であればPython上で以下を実行
```Python
>>> from pip._internal.pep425tags import get_supported
>>> get_supported()
[('cp37', 'cp37m', 'win_amd64'), ('cp37', 'none', 'win_amd64'), ('py3', 'none', 'win_amd64'), ('cp37', 'none', 'any'), ('cp3', 'none', 'any'), ('py37', 'none', 'any'), ('py3', 'none', 'any'), ('py36', 'none', 'any'), ('py35', 'none', 'any'), ('py34', 'none', 'any'), ('py33', 'none', 'any'), ('py32', 'none', 'any'), ('py31', 'none', 'any'), ('py30', 'none', 'any')]
```
## pipに対応している.whlファイルをインストールする
[OpenCVのダウンロードサイト](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)から対応しているwhlファイルをダウンロードする。
whlファイルのダウンロード場所でpipを用いてインストールする。
```

```

[参考サイト](https://qiita.com/kenta1984/items/16a14f3bfaf1f257c585)
