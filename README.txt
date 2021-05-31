- 説明
最安値ドットコムから、JANコードを元に現在の最安値価格を取得する
https://www.saiyasune.com/

- 処理概要
対象スプレッドシートのシート1の、A列にあるJANコードを取得する。
JANコードをもとに最安値ドットコムで現在の最安値価格を取得する。
対象スプレッドシートのシート1の、B列に現在の値段を出力する。

- 実行方法
scraping.py のあるフォルダへ移動
py scraping.py で実行

- 環境構築
1.インストール（Python・pip が使える状態が前提）
pip install selenium
pip install chromedriver-binary
pip install gspread
pip install oauth2client

2.情報を調べるためのスプレッドシートを準備
以下のサイトを参照する（現状UIがサイトと少し異なる）
https://tanuhack.com/operate-spreadsheet/

3.chromedriver を用意する
https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19/
chromedriver_win32.zip をダウンロードし、解凍する
chromedriver.exe を scraping.py のあるフォルダにコピーする

4.settings.py への設定
settings.py を開いて、以下の '' の間に提示する情報を入れる
    json_key = ''
    spredsheet_key = ''
GitHub上に載せられない情報なので、GitHub以外の領域で情報を提供します

5.スプレッドシートへのアクセス(開発者本人用)
スプレッドシートへのアクセス用jsonファイルは別途保管

- 注意点
サイトにも記載されているが、google側で以下の提示がされている
    1. ユーザーごとに100秒あたり100件のリクエスト
    2. 1回のプログラムで設定できる最大値は1,000件まで
    3. さらに1秒あたり10件まで