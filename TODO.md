# のれん様プログラム
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
受け取ったセンサー情報をOSCでサーバーに送信する

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

## HumanIntelligence
サーバーに強制実行するものがないか見に行く

## StatusManager
x 時間を教える
x センサー情報を教える
天気情報を教える
強制実行するセリフを教える

## Action
x 起動する条件にあったら、セリフとツイートをする
x 起動したら、しばらく休む

## NorenSama
定期的にStatusManagerに情報を教えてもらう
x 定期的にActionに起動するかどうか聞いて回る
x 起動したものがあれば、しばらく休む
RTがあったときに、起動中のActionが終わるのを待って、チロリンと鳴らす

# ディスプレイプログラム
## Updater
ツイートの更新を取得する
取得したら、再描画

# 人力AI
## ForceAction
強制的に実行するアクションを選んで、サーバーに送る

## ForceLine
アクションを指定せずに、喋る文章を選ぶ、サーバーに送る

# 音声合成APIについて
http://voicetext.jp/

# ポケットWifiの設定
プライバシーセパレーターはOFFにすること
