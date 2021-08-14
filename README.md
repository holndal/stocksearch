# Stock Search Repository
入荷通知を行うプログラムの一部。

# 注意事項
既にプログラムを販売済みなので許可を取ってプログラムの一部のみこのレポジトリに載せています。肝が載ってないのはご了承ください。

# アプリの概要
一定時間毎に在庫の検出を行い、在庫を検知すると通知を行うアプリケーション。
基本的にAmazon Product Advertising APIや楽天市場API、Yahoo APIを利用して在庫の検出を行う。
それに加えてクローリングが禁止されていないではクローリングを行い在庫の検知を行う。

※販売サイトに迷惑をかけないようクローリングの頻度は低めに設定する。

# 使用言語
Python 3
HTML (はてなブログに投稿する際に使用)

# 注力した機能や工夫した点
## 並列実行
単純なfor文だけでプログラムを書くと「在庫を検出」→「通知」の間にラグが発生してしまう為、並列処理を行う
[concurrent.futures](https://docs.python.org/ja/3/library/concurrent.futures.html)
を用いて複数の関数を並列で実行するようにした。
ただし「同一サイトに対するアクセスの並列化」は避けた。ｚ

## 連携アプリ
在庫を検知するとTwitter Discord LINE email はてなブログに情報を送る機能を実装しました。
更にGoogle Sheets APIを用いることで現在の在庫状況はどうなのか簡単に確認できるようにしていました。

# 環境
どの環境も基本的にPython3が入っているためPip3をインストール・必要なパッケージをインストールしたのみ

## 開発環境1
自宅のマシンを使用
OS Ryzen 7 5800X
RAM 16GB
GPU RTX3060Ti
OS Windows 10

Jupyter-Notebook上で開発を行った。

## 本番環境1 VPC
[AWS EC2 t2.micro](https://aws.amazon.com/jp/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc)
[Vultr](https://www.vultr.com/)
OS Ubuntu Server 20.04 LTS

## 本番環境2 ローカル
本番環境1は運用コストが高いためローカル環境に移行しました。

Raspberry Pi 4 Modeb B
OS Ubuntu Server 20.04 LTS
