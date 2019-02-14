# Gitの基本

## Gitインストール（window）
https://gitforwindows.org/ よりインストール（設定は初期でOK）
## Gitの確認
ターミナル（Git Bash）を開く。以下コマンドを入力
- $ git version

## gitの初期設定
### Gitの設定ファイルは以下三種類
- system  当該マシンの全ユーザに関する設定
- global  当該ユーザに関する設定
- local   特例のディレクトリ（リポジトリ）に関する設定

### 今回はglobalの設定を行う  
- $ git config --global user.name "github user.name"  //githubのユーザネーム  
- $ git config --global use.email github@example.com  //githubのメアド  
- $ git config --global core.editor "atom --wait"     //gitで使うエディタ vs codeなら"code --wait"  

### 設定の確認
- $ git config --list （個別に見たい場合は$ git config use.emailのようにする）

### globalのgitconfigの置き場
ログインユーザのHOMEディレクトリ配下の .gitconfig（C:\Users\{username}\.gitconfig）
ターミナルから以下のコマンドでも見れる。
- $ cat ~/.gitconfig

# Gitの基本操作
ローカル（自分のPC）は3つのエリアに分かれている。
- ワークツリー（ファイルを変更する作業場）
- ステージ（コミットの準備をする）
  - git addで変更点をインデックスに保存
- ローカルリポジトリ（スナップショットを記録）
  - git commitでステージのインデックスに保存されているファイルのスナップショットをとる

# Gitのデータ管理
git addやgit commitをすると、ローカルリポジトリに「圧縮ファイル」「ツリーオブファイル」「コミットオファイル」が作成される。
Gitではこれらのファイルを「Gitオブジェクト」と呼び、「.git/object」ディレクトリの下に保存される。
各ファイルの説明は以下のとおりである。
- Gitオブジェクト
  - 圧縮ファイル（blobオブジェクト）
    - git addをした際にリポジトリに作成される。正確には「blobオブジェクト」と言い、ファイルの中身を圧縮しただけのもの
  - ツリーファイル（treeオブジェクト）
    -  圧縮ファイルには圧縮前の元々のファイル名の情報が入っていない。ファイル名とファイルの中身の組み合わせ（ファイル構造）を保存するためのものがツリーファイルであり、正確には「treeオブジェクト」言う
  - コミットファイル（commitオブジェクト）
    - いつ、誰が、何を、何のために、ファイルを変更したのかという情報を保存するもの。正確には「commitオブジェクト」と言う

## 実際の動きを見てみよう(/・ω・)/
### ローカルリポジトリの作成
ターミナル（Git Bach）を開く。ホームディレクトリへ移動する。
- $ mkdir sample  //ホームディレクトリ直下に「sampleディレクトリ」を作成
- $ cd sample //sampleディレクトリに移動
- $ git init  //現在のディレクトリを（ローカル）リポジトリとして指定する（リポジトリの新規作成）

「sampleディレクトリ」内に「.gitディレクトリ」が作成されているのを確認する。隠しファイルなので注意。これが作成されていればローカルリポジトリの作成は成功だょ

### ファイルのステージング
- $ echo 'Heloo,World!' >hello  //sampleディレクトリ内にhelloファイルを作成
- $ git hash-object hello
e965047ad7c57865823c7d992b1d046ea66edf78


このような文字列が返ってくる。
返ってきた文字列は「ハッシュID」と言う。ハッシュIDのうち、先頭2文字をディレクトリ名に、その後ろをファイル名にして圧縮ファイルを保存する。
では、実際に圧縮ファイルを作成してみよう。

- $ git add hello //ファイルをステージングする

ここで「.git/object」ディレクトリを確認すると「e9ディレクトリ」内に「65047ad7c57865823c7d992b1d046ea66edf78」という圧縮ファイルが作成されている。先ほどのハッシュIDと同じことを確認しよう。
※ハッシュIDはファイルの中身に対して一意なもの。中身が同じものなら何度git addしようとも圧縮ファイルが追加で作られることはない。

### ツリーオブジェクトの確認
ファイルの中身の圧縮ファイルまでは作成出来た。次に元々のファイル名とファイルの中身の組み合わせ（ファイル構造）を保存する。
- $ git commit -m 'add hello' //コミットしてツリーオブジェクトを作成
[master (root-commit) 41d0cd8] add hello
 1 file changed, 2 insertions(+)
 create mode 100644 hello
- $ git cat-file -p master^{tree}  //masterブランチ上での最後のコミットが指しているツリーファイルの中身を表示する。
100644 blob e965047ad7c57865823c7d992b1d046ea66edf78    hello

最後のコミットが指しているtreeオブジェクトには、blobオブジェクト「e965047ad7c57865823c7d992b1d046ea66edf78」が「hello」というファイル名だということが保存されている。

### コミットファイルの確認
ツリーファイルが作成されたことで、ファイル構造を追えるようになった。では、いつ、誰が、何を、何のために変更したのかを確認してみる。
- $ git cat-file -p HEAD  //最新のコミットファイルの中身を表示する
tree 90fa7e05d3e0a8c71be3b43fd1cae61d1b8f6e0a
author eiji-noguchi <github@example.com> 1549210901 +0900
committer eiji-noguchi <github@example.com> 1549210901 +0900

  add hello

まず、コミットした時点のtree「90fa7e05d3e0a8c71be3b43fd1cae61d1b8f6e0a」が保存されている。これはこのプロジェクトの一番上のディレクトリのツリーファイルとなる。次に作成者の情報とコミットメッセージが保存されている。
ちなみにこのtreeファイル内を見ると、先ほどのblobオブジェクト確認できる
- $ git cat-file -p 90fa  //treeファイル中身を確認する
100644 blob e965047ad7c57865823c7d992b1d046ea66edf78    hello


### ここまでのまとめ
ここまでファイルの作成からステージング、そしてコミットまでを行ってきた。ここでblobとtreeの関係性をまとめる。
- blob:ファイル
- tree:ディレクトリ
つまり、現在ローカルリポジトリには「90fa7e05d3e0a8c71be3b43fd1cae61d1b8f6e0a」のディレクトリ（tree）下に「e965047ad7c57865823c7d992b1d046ea66edf78」というファイル（blob）が存在しているということ。


### ファイルの変更
最後にファイルを編集し、その変更をコミットした場合の動きを確認してみよう(´・ω・｀)
- $ vim hello //helloディレクトリを編集し保存する
- $ git add hello
- $ git commit -m 'update hello'
- $ git cat-file -p HEAD  //HEADコマンド：今自分がいるブランチの最新のコミット
tree 9e610c2a62cae34a4d476e1d4eeb3d057a43a339
parent 41d0cd83f6b491c66fd4f009ef77052a5c8d4673
author eiji-noguchi <github@example.com> 1549211186 +0900
committer eiji-noguchi <github@example.com> 1549211186 +0900

  update hello

編集したディレクトリをコミットし、再度コミットファイルの中身を確認してみると、「**parent**」と言う親コミット情報を保存している。Gitはこのように親コミットを保存することによってコミットの履歴を辿れるようにしている。
また、ファイルが変更された場合、変更ファイルやそれらに該当しているtreeのハッシュIDは更新される。

### treeオブジェクトの追加
次にtreeオブジェクトの下に更にtreeオブジェクトを作成する。


- $ mkdir subdir
- $ echo 'Goodbye,world' >subdir/goodbye
- $ git add subdir
- $ git commit -m 'add goodbye'
[master 79d9920] add goodbye
 1 file changed, 1 insertion(+)
 create mode 100644 subdir/goodbye
- $ git cat-file -p HEAD
tree f51ccf26d3de80812e99db8abe654074786b39f0
parent e4f4a712740c385e0da4eefefee96f6ccbe07f2d
author eiji-noguchi <eiji.program@gmail.com> 1549774515 +0900
committer eiji-noguchi <eiji.program@gmail.com> 1549774515 +0900

  add goodbye
- $ git cat-file -p master^{tree}
100644 blob c25857953927ed759aa024b43432a278e1fb163d    hello
040000 tree 56e8dcdd51f41264863ffbab155ffea2bc342385    subdir

つまりmasterブランチ上のトップにはtree(ディレクトリ)「f51c...」があり、その下にblob(helloファイル)「c258...」とtree(subdirディレクトリ)「56e8...」が存在している。
ここで注意すべきはtreeオブジェクトは自分の直下のファイルやディレクトリしか認識していないこと。先ほど作成した「goodbyeファイル」についてはmasterブランチ上のトップのtree「f51c...」ではなく、その下のtree「56e8...」が認識している。
- $ git cat-file -p 56e8
100644 blob c90b99c703da8e3bcf6c34a2291bccbb02b6c6bc    goodbye

ここで「goodbyeファイル」を編集し、コミットした場合、blob(goodbye)「c90b...」、tree「56e8...」、tree「f51c...」のハッシュIDが変更される。
ちなみにblobやtreeの前についている数字は型である。
- 100644:ファイル
- 040000:ディレクトリ

# 備考
##  Gitコマンドメモ
- リポジトリの削除
  - rm -rf .git
- 変更したファイルの状態確認（ワークツリーとステージの比較、ステージとリポジトリの比較）
  - git status
- ステージング前のファイルの変更点確認（ワークツリーとステージの比較）
  - git diff <ファイル名>
- ステージングされたファイルの変更点確認（ステージとリポジトリの比較）
  - git diff --staged
- 変更履歴の確認
  - git log
  - git log --oneline //一行で表示
  - git log -p <ファイル名>  //ファイルの変更差分を表示する
  - git log -n <コミット数>  //表示するコミット数を制限する
- リポジトリとワークツリーからファイル、ディレクトリの削除
  - git rm <ファイル名>
  - git rm -r <ディレクトリ名>
- リポジトリからのみファイルの削除（ワークツリーには残る）
  - git rm --cached <ファイル名>
- ファイルの移動（ファイル名の変更）
  - git mv <旧ファイル名> <新ファイル名>
- リモートリポジトリからコピーの作成
  - git clone <リポジトリ名>
- originというショートカットでurlのリモートリポジトリを登録する
  - git remote add origin <リモートリポジトリのURL>
- ローカルリポジトリの内容をリモートリポジトリに登録する
  - git push <リモート名> <ブランチ名>
- 「.gitignore」ファイル内にバージョン管理したくないファイル名を記載することで、そのファイルを無視できる
- ファイルへの変更を取り消す
  - git checkout -- <ファイル名> //ワークツリーのファイルをステージから取得し反映させる
  - git checkout -- <ディレクトリ名> //ワークツリーのディレクトリをステージから取得し反映させる
  - git checkout -- . //全変更を取り消す
- ステージした変更の取り消し
  - git reset HEAD <ファイル名>  //リポジトリから直前のコミットの情報を取得し、ステージの内容を上書きする
  - git reset HEAD <ディレクトリ名>
  - git reset HEAD <ファイル名>
- 直前のコミットをやり直す
  - git commit --amend  //現在のステージの内容で、直前のコミットを上書きする ※push後には使ってはいけない
