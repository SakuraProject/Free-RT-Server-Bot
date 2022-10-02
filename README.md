# Free-RT-Server-Bot
freeRT公式サーバー専属botです。まだ機能は作成されていませんが作成予定の機能は以下の通りです。
* よくある質問
* (free) RTダウン通知
* 質問自動回答ヘルパー
* etc...
## Installation
### Depedencies
必要なものです。
- Python 3.8
- git
- [requirements.txt]にあるもの全て。
    - jishaku
    - ujson
    - discord.py 2.1.0a
### 起動手順
  1. 必要なものをpip install -r requirements.txtでインストールをします。
  2. 必要なTOKENなどをauth.template.jsonを参考にauth.jsonに書き込む。
  3. `python3 main.py`で実行する。

[requirements.txt]: https://github.com/free-RT/Free-RT-Server-Bot/blob/main/requirements.txt
