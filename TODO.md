# のれん様プログラム
## 残タスク
x 人感センサーのチューニング
x 実際使用するMacでのテスト
x 加速度センサーのチューニング
x ツイッターに対するレスポンス
x 天気情報の取得
x 天気情報に対するレスポンス
x 各種ふるまいの制作
セリフを言うタイミングのチューニング
１時間で、どれだけパケット消費するかのチェック
起動終了のマニュアルの作成
ウェブソケットがIPを指定しないと通信できないので、治す→引数に指定する

x Twitterを別スレッドに
x ファイル名のタイポを治す
強制アクションの仕組み
x 音声ファイルの再生開始をできるだけ早く

## 余裕が出たら
人力AIのUIのブラッシュアップ
ツイッター画面に対して、加工する

## Sensor
センサーにデータが欲しいと伝える
センサーから、データを受け取る
x Serial
x obniz
espのみ
raspberry pi

https://qiita.com/ie4/items/ae850cdb2c617f3fd6af
https://qiita.com/juosugi/items/66f25cc60734d17bc7f0
http://arakaze.ready.jp/archives/4278
https://www.slideshare.net/lemiyachi/espwroom02
→よくわからん

### obniz
x 受け取ったセンサー情報をOSCでサーバーに送信する

## Speaker
x 指定されたファイルを再生する

## Tweet
x 指定された文言を投稿する
RTがあったら、教える

## IFTTT
インスタグラムの投稿があったら
ツイッターでフォローされたら
ツイッターでRTされたら
ツイッターでメンションされたら
フォロワーの数はできる？

## Weather
一定期間ごとに、天気予報を見に行く
https://qiita.com/Barbara/items/93ae7969691164c7c2bc

## HumanIntelligence
x サーバーに強制実行するものがないか見に行く

## StatusManager
x 時間を教える
x センサー情報を教える
天気情報を教える
x 強制実行するセリフを教える

## Action
x 起動する条件にあったら、セリフとツイートをする
x 起動したら、しばらく休む

## NorenSama
x 定期的にStatusManagerに情報を教えてもらう
x 定期的にActionに起動するかどうか聞いて回る
x 起動したものがあれば、しばらく休む
RTがあったときに、起動中のActionが終わるのを待って、チロリンと鳴らす

# ディスプレイプログラム
## Updater
x ツイートの更新を取得する
x 取得したら、再描画

# 人力AI
x pythonでサーバーを立ち上げる
x POSTにデータを入れて、セリフを実行する

## ForceSerif
x アクションを指定せずに、喋る文章を選ぶ、サーバーに送る

# 音声合成APIについて
http://voicetext.jp/

# ポケットWifiの設定
プライバシーセパレーターはOFFにすること

https://qiita.com/makaishi2/items/ae83828a711d0d946011
https://qiita.com/makaishi2/items/ed9d4412331d7d65fde5
https://qiita.com/makaishi2/items/5c7b1b6a72b6938cf3d2
